from django.db import models
from account import models as acc_models


class Child(models.Model):
    name = models.CharField(max_length=50, blank=False)
    dob = models.DateField()
    parent = models.ForeignKey(
        'account.ParentUser', related_name='children', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


