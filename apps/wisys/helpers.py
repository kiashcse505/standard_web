import traceback
from datatableview.helpers import keyed_helper
from django.core.mail import send_mail
from django.template import loader
#import dpath
# from apps.prms.constants import RAG_CHOICES
from apps.wisys.exceptions import WisysRestFrameworkException
from .php import *
import json
from rest_framework import status
from rest_framework.response import Response
from django.core.mail import EmailMultiAlternatives
import logging
defaultLogger = logging.getLogger(__name__)

def create_or_append(map,key,value):
        return map.setdefault(key,[]).append(value)


def get_request_payload( request, method='post' ):

    jsonData = request.DATA.get('data',None)
    if method == 'get' :
        jsonData = request.GET.get('data',None)

    if jsonData is not None:
        try:
            request_json = json.loads(jsonData)
            return request_json
        except ValueError:
            return Response( { 'error' : 'JSON Parse Error' , 'data_recieved' : jsonData }, status= status.HTTP_400_BAD_REQUEST )
    else:
        return Response( { 'error' : 'Invalid JSON' , 'data_recieved' : jsonData }, status= status.HTTP_400_BAD_REQUEST )

    return None


def give_response_with_msg( message, status ):
    return Response( message , status )

def give_400_response_with_error(error_msg ):
    return give_response_with_msg( { 'error': error_msg }, status = status.HTTP_400_BAD_REQUEST )

def give_404_response_with_error(error_msg ):
    return give_response_with_msg( { 'error': error_msg }, status = status.HTTP_404_NOT_FOUND )


def give_api_exception_with_message( message , status ):
    raise WisysRestFrameworkException( message, status )

def give_api_404_exception_with_message( message ):
    raise WisysRestFrameworkException( message, status.HTTP_400_BAD_REQUEST )


def validate_json_for_keys(keys, json , message_pad = None ):
    print message_pad

    response = True
    if is_string(keys):

        if keys not in json:
            # print "%s | %s | %s | \\n" % ( keys, json , message_pad )
            message = '%s is required' % message_pad
            # if message_pad is not None:
            #     message = '%s -> %s is required.' % ( message_pad , keys )

            return Response( { 'error': message }, status = status.HTTP_400_BAD_REQUEST )

        return response

    else:
        for a_tag in keys:
            new_tag = " %s " % a_tag
            if message_pad is not None:
                new_tag = "%s -> %s " % ( message_pad, a_tag )

            response =  validate_json_for_keys( a_tag, json, new_tag )
            if response is not True:
                return response

            if is_array(keys[a_tag]):
                response = validate_json_for_keys( keys[a_tag], json[a_tag], new_tag )
                if response is not True:
                    return response


        return response


def get_flat_options_dict( options , keyPad , flatOptions = {} ):

    for aKey in options:
        if is_array(options[aKey]):
            flatOptions = get_flat_options_dict( options[aKey], aKey, flatOptions )
        else :
            key = '%s_%s' % ( keyPad, aKey)
            flatOptions[str(key)] = options[aKey]

    return flatOptions

## Refector Needed
# def reverse_flat_option_dict( keys, flat_dict ):
#     reversed_dict = {}
#     for a_key in keys:
#         reversed_dict[a_key] = {}
#         for a_flat_dict in flat_dict:
#             if a_flat_dict.key.startswith(a_key):
#                 new_key = a_flat_dict.key.replace( '%s_' % a_key, '' )
#                 value = a_flat_dict.value
#                 extra = a_flat_dict.extra
#                 dict_data = { 'value': value }

#                 try:
#                     if extra['prms']['rag_color']:
#                         dict_data.update( { 'color' : get_key_from_tuple( extra['prms']['rag_color'], RAG_CHOICES ) } )
#                 except:
#                     pass

#                 reversed_dict[a_key][new_key] = dict_data

#     return reversed_dict


def handle_uploaded_file(location,file):

    # dirPath = location.split("/")[-1]
    # os.makedirs(dirPath)

    with open(location, 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)

def validateEmail( email ):
    from django.core.validators import validate_email
    from django.core.exceptions import ValidationError
    try:
        validate_email( email )
        return True
    except ValidationError:
        return False


def send_plain_email_with_context( emails, from_email, subject_template_name, email_template_name, context):

    subject = loader.render_to_string(subject_template_name, context)
    # Email subject *must not* contain newlines
    subject = ''.join(subject.splitlines())
    email = loader.render_to_string(email_template_name, context)
    return send_mail(subject, email, from_email, emails )



def send_html_email( emails, from_email, subject_template_name, email_template_name, context):

    subject = loader.render_to_string(subject_template_name, context)
    subject = ''.join(subject.splitlines())

    html_content = loader.render_to_string(email_template_name, context)

    msg = EmailMultiAlternatives(subject, html_content, from_email, emails )
    msg.attach_alternative(html_content, "text/html")
    msg.send()



def get_value_from_tuple( key, tuple ):
    try:
        for an_item in tuple:
            print an_item
            if key == an_item[1]:
                return an_item[0]
    except Exception as ex:
        print ex
        return ""

def get_key_from_tuple( value, tuple ):
    try:
        return tuple[ value - 1][1]
    except Exception as ex:
        print ex
        return ""

def get_float_value( value ):
    try:
        return float(value)
    except:
        return 0.0

def ex_print_trace():
    ex = traceback.format_exc()
    print ex

def ex_log_trace():
    ex = traceback.format_exc()
    defaultLogger.error(ex)

# def validate_json( key, message , json):
#
#      if key not in json :
#          return Response( { 'error': message }, status = status.HTTP_400_BAD_REQUEST)
#      return True

class InlineClass(object):
    def __init__(self, dict):
	self.__dict__ = dict

class Inline(object):
    pass


@keyed_helper
def link_to_model(instance, text=None, *args, **kwargs):
    """
    Returns HTML in the form

        <a href="{{ instance.get_absolute_url }}">{{ instance }}</a>

    If ``text`` is provided and is true-like, it will be used as the hyperlinked text.

    Else, if ``kwargs['default_value']`` is available, it will be consulted.

    Failing those checks, ``unicode(instance)`` will be inserted as the hyperlinked text.

    """
    if not text:
        text = kwargs.get('default_value') or unicode(instance)

    try:
        url = instance.get_absolute_url()
    except:
        url = args.get('url')

    return u"""<a href="{}">{}</a>""".format(url, text)


def get_age_from_birthdate(birthdate):
    from datetime import date
    days_in_year = 365.2425

    age = int((date.today() - birthdate).days/days_in_year)

    return age

#String Helpers

def api_delay(delay_time):
    import time
    time.sleep(delay_time) # delays for time seconds


def get_timestamp_from_datetime(datetime_obj):
    return int(time.mktime( datetime_obj.timetuple())*1000)