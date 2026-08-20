from django.contrib import admin

from core.models import Room


# admin.site.register(Room)


class roommodel(admin.ModelAdmin):
    list_display = ('title', 'description')

    # list_filter = ("location")


admin.site.register(Room, roommodel)



