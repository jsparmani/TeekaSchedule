from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.Cluster)
admin.site.register(models.Locality)
admin.site.register(models.Ward)
