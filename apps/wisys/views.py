from operator import or_
from time import  time
from datatableview.views import DatatableView, dateutil
from django.core.urlresolvers import reverse
from django.db.models import Q
from django.shortcuts import render_to_response
from django.template.response import TemplateResponse
from django.views.generic import CreateView, UpdateView
from django.views.generic.detail import SingleObjectMixin

#from eztables.views import RE_FORMATTED
from apps.wisys import helpers
from apps.wisys.forms import SystemLogoForm, SitenameForm
from apps.wisys.models import Settings
from mhealthcare import settings


def generic_view(request,
                        template_name='wisys/generic.html',
                        current_app=None, extra_context=None):
    context = {}
    if extra_context is not None:
        context.update(extra_context)
    return TemplateResponse(request, template_name, context,
                            current_app=current_app)


class IrDatatableView(DatatableView):

    pk_url_kwarg = 'pk'

    extra_context = {}

    def get_hidden_row_selection_box(self, instance, *args, **kwargs):
       return '<input class="user-checkbox" type="checkbox" style="display: none" value="%s">' % instance.id

    def get_row_selection_box(self, instance, *args, **kwargs):
       return '<input class="user-checkbox" type="checkbox" value="%s">' % instance.id

    def get_friendly_name(self, instance, *args, **kwargs):
        function_name = 'get_%s_display' % kwargs['field_data'][1]
        return getattr(instance, function_name )()

    def get_excerpt(self, instance, *args, **kwargs):
        return instance.text

    def get_default_date_format(self, instance, *args, **kwargs):
        return instance.created_at.strftime( "%a, %d %b %Y %H:%M:%S" )


    def get_context_data(self, **kwargs):

        context = super(IrDatatableView, self).get_context_data(**kwargs)
        try:
            context.update(**self.extra_context)
        except:
            raise Exception("Unable to add extra context")

        return context

    def column_search(self, queryset):
        print self.dt_data['iColumns']
        '''Filter a queryset with column search'''
        for idx in xrange(self.dt_data['iColumns']):
            search = self.dt_data['sSearch_%s' % idx]
            if search:
                if hasattr(self, 'search_col_%s' % idx):
                    custom_search = getattr(self, 'search_col_%s' % idx)
                    queryset = custom_search(search, queryset)
                else:
                    field = self.get_field(idx)
                    fields = RE_FORMATTED.findall(field) if RE_FORMATTED.match(field) else [field]
                    if self.dt_data['bRegex_%s' % idx]:
                        criterions = [Q(**{'%s__iregex' % field: search}) for field in fields if self.can_regex(field)]
                        if len(criterions) > 0:
                            search = reduce(or_, criterions)
                            queryset = queryset.filter(search)
                    else:
                        for term in search.split():
                            criterions = (Q(**{'%s__icontains' % field: term}) for field in fields)
                            search = reduce(or_, criterions)
                            queryset = queryset.filter(search)
        return queryset



    def get_queryset(self):
        qs = super(IrDatatableView, self).get_queryset()

        try:
            '''Apply Datatables sort and search criterion to QuerySet'''
            # Perform column search
            qs = self.column_search(qs)
            # Return the ordered queryset

        except Exception, ex:
            print ex

            pass

        return qs


    # def get(self, request, *args, **kwargs):
    #     return super(IrDatatableView, self).get(request,args, kwargs )


class IrBaseMixin(SingleObjectMixin):
    success_message = "Task done successfully"

    def get_context_data(self, *args, **kwargs):
        context = super(IrBaseMixin, self).get_context_data(*args, **kwargs)
        context['STATIC_URL'] = settings.STATIC_URL
        return context


from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

class LoginRequiredMixin(object):
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch(*args, **kwargs)


from django.utils.decorators import method_decorator

def class_view_decorator(function_decorator):
    """Convert a function based decorator into a class based decorator usable
    on class based Views.

    Can't subclass the `View` as it breaks inheritance (super in particular),
    so we monkey-patch instead.
    """

    def simple_decorator(View):
        View.dispatch = method_decorator(function_decorator)(View.dispatch)
        return View

    return simple_decorator

from django.utils.decorators import method_decorator
from apps.users.decorator import super_user_member_required
class SettingMixin(object):
    model = Settings
    context_object_name = "admin-setting"
    paginate_by = 10

    def get_success_url(self):
        return reverse('system-settings')

    def get_queryset(self):
        return Settings.objects.all()

class SettingsView(SettingMixin, CreateView):
    form_class = SystemLogoForm
    template_name = 'setting/form.html'

    @method_decorator(super_user_member_required)
    def dispatch(self, *args, **kwargs):
        return super(SettingsView, self).dispatch(*args, **kwargs)

from django.contrib.sites.models import Site


@login_required
def listSitenameView(self,*args, **keyargs):
    sites = Site.objects.all()
    return render_to_response('setting/site_home.html',{'sites':sites})
class SitenameMixing(object):
    model = Site
    context_object_name = "site-settings"
    paginate_by = 1

    def get_success_url(self):
        return reverse('domain-list')

    def get_queryset(self):
        return Site.objects.all()

class SitenameView(SitenameMixing,UpdateView):
    form_class = SitenameForm
    template_name = 'setting/site_form.html'


class DomainListView(IrDatatableView):
    template_name = 'setting/site_home.html'

    def get_queryset(self):
        return Site.objects.all()

    datatable_options = {
        'structure_template': "wisys/datatable/default_table.html",
        'columns': [
            ('#','id', 'get_row_selection_box' ),
            'domain',
            'name',

        ],
        'unsortable_columns': ['#'],

    }


class DomainhomeView(DomainListView):
    pass

