from django.contrib import admin

from unielv.models import *

class ElevatorAdmin(admin.ModelAdmin):
    list_display = ('group', 'dong', 'min_floor', 'max_floor')
    list_filter = ['group']

admin.site.register(Elevator, ElevatorAdmin)
