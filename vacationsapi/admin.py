from django.contrib import admin

from vacationsapi.models import Vacations


class VacationsAdmin(admin.ModelAdmin):
    list_display=['place','price','travel','food','accomodation']

# Register your models here.
admin.site.register(Vacations,VacationsAdmin)