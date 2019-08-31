from django.db import models
from account import models as acc_models


class Child(models.Model):
    name = models.CharField(max_length=50, blank=False)
    dob = models.DateField(blank=False)
    parent = models.ForeignKey(
        'account.ParentUser', related_name='children', on_delete=models.CASCADE, blank=True, null=True)



    def __str__(self):
        return self.name


class VaccinationData(models.Model):

    name = models.CharField(max_length=50, blank=False)
    duration = models.BigIntegerField()

    class Meta:
        ordering = ['duration']

    def __str__(self):
        return self.name


class Vaccine(models.Model):

    child = models.ForeignKey(
        'parent.Child', related_name='vaccinnes', on_delete=models.CASCADE)
    name = models.CharField(max_length=50, blank=False)
    date = models.DateField()
    status = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name}-{self.child}'
