from django.utils.translation import gettext_lazy as _
from django.db import models
import uuid
from django.conf import settings
import pytz

tz = pytz.timezone(settings.TIME_ZONE)


class BaseModel(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        unique=True,
        verbose_name=_("ID"),
    )
    is_deleted = models.BooleanField(default=False, verbose_name=_("удаленный?"))
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name=_("дата создания")
    )
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("дата изменения"))

    def get_date(self):
        return self.created_at.astimezone(tz).date()

    def get_hour(self):
        return self.created_at.astimezone(tz).time()

    class Meta:
        abstract = True