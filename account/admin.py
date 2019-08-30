from django.contrib import admin
from . import models

admin.site.register(models.WardUser)
admin.site.register(models.ANMUser)
admin.site.register(models.ParentUser)
admin.site.register(models.ClusterUser)
admin.site.register(models.OTP)
