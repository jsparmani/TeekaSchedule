from django.contrib import admin
from . import models
# Register your models here.
from import_export.admin import ImportExportModelAdmin


class LocalityAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name']


admin.site.register(models.Cluster)
admin.site.register(models.Locality, LocalityAdmin)
admin.site.register(models.Ward)
admin.site.register(models.Hosptial)


@admin.register(models.District)
class ViewAdmin(ImportExportModelAdmin):
    pass
