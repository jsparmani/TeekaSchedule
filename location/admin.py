from django.contrib import admin
from . import models
# Register your models here.


class LocalityAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name']

admin.site.register(models.Cluster)
admin.site.register(models.Locality, LocalityAdmin)
admin.site.register(models.Ward)
admin.site.register(models.Hosptial)
admin.site.register(models.District)

