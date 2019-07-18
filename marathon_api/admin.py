from .models import Event, Photo
from django.contrib import admin


class PhotoAdmin(admin.ModelAdmin):

    def has_add_permission(self, request, obj=None):
        return True

    def has_view_permission(self, request, obj=None):
        return True
    
    def has_change_permission(self, request, obj=None):
        return True

admin.site.register(Event)
admin.site.register(Photo, PhotoAdmin)
