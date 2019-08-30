from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.Child)
admin.site.register(models.VaccinationData)
admin.site.register(models.Vaccine)
