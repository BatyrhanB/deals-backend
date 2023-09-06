from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _


class ImageTagAdminMixin:
    def photo_tag(self, obj):
        if obj.photo:
            return format_html(
                '<img src="{}" width="150" height="150" '
                'style="object-fit:contain"/>'.format(obj.photo.url)
            )

    def icon_tag(self, obj):
        if obj.icon:
            return format_html(
                f'<img src="{obj.icon.url}" width="150" height="150"'
                'style="object-fit:contain;" style="border-radius: 10px;"/>'
            )

    icon_tag.short_description = _("icon")
    photo_tag.short_description = _("photo")
