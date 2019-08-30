from django.contrib import admin
from . import models
# Register your models here.


class VaccineAdmin(admin.ModelAdmin):
    list_display = ['name', 'status']


admin.site.register(models.Child)
admin.site.register(models.VaccinationData)
admin.site.register(models.Vaccine, VaccineAdmin)
