from django.db import models
from json_field import JSONField

from apps.wisys.constants import ACTIVE, INACTIVE, DELETED, ARCHIVED

class StatusQuerySet(models.query.QuerySet):

    def active(self):
        return self.filter(status=ACTIVE)

    def inactive(self):
        return self.filter(status=INACTIVE)


    def deleted(self):
        return self.filter(status=DELETED)

    def archived(self):
        return self.filter(status=ARCHIVED)


class StatusManager(models.Manager):

    def get_queryset(self):
        return StatusQuerySet(self.model, using=self._db)

    def active(self):
        return self.get_queryset().active()

    def inactive(self):
        return self.get_queryset().inactive()

    def deleted(self):
        return self.get_queryset().deleted()

    def archived(self):
        return self.get_queryset().archived()



class AbstractBase(models.Model):

    # def custom_query(self, raw_query):
    #     from django.db import connection
    #     cursor = connection.cursor()
    #     cursor.execute(raw_query)
    #     result_list = []
    #     for row in cursor.fetchall():
    #         result_list.append(self.model(row))
    #     return result_list
    # def __init__(self):
    #     # if hasattr(self,'status'):
    #     setattr(self, 'status_objects', StatusManager())

    objects = models.Manager()
    status_objects = StatusManager()

    def auto_update_slug(self):
        pass

    class Meta:
        abstract = True


class SettingsBase(AbstractBase):

    key = models.CharField(max_length=250)
    value = models.TextField()
    extra = JSONField(default="{}",blank=True)

    class Meta:
        abstract = True;


class Settings(SettingsBase):

    class Meta:
        db_table = 'ir_system_settings'

class SettingsLogo(AbstractBase):
    logo_image = models.ImageField(upload_to='custom/')

    def get_logo_image(self):
        if self.logo_image:
            return self.logo_image
