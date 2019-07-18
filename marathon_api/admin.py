from django.contrib import admin
from marathon_api.models import Photo, Event


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'original', 'watermark', 'event', 'created_by')
    fields = ('original', 'watermark', 'event')

    def has_add_permission(self, request, obj=None):
        return True

    def has_view_permission(self, request, obj=None):
        return True

    def has_change_permission(self, request, obj=None):
        return True


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
