from django.contrib import admin
from marathon_api.models import Photo, Event


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'original', 'watermark', 'event')
    fields = ('original', 'watermark', 'event')


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
