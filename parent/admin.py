from django.contrib import admin
from . import models
# Register your models here.


class VaccineAdmin(admin.ModelAdmin):
    list_display = ['name', 'child', 'status']
    list_filter = ['child']


class ReminderAdmin(admin.ModelAdmin):
    list_display = ['parent', 'date', 'vaccine']

class ReminderANMAdmin(admin.ModelAdmin):
    list_display = ['child', 'date', 'vaccine']


admin.site.register(models.Child)
admin.site.register(models.VaccinationData)
admin.site.register(models.ReminderANM, ReminderANMAdmin)
admin.site.register(models.Vaccine, VaccineAdmin)
admin.site.register(models.Reminder, ReminderAdmin)
