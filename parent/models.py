from django.db import models
from account import models as acc_models


class Child(models.Model):
    name = models.CharField(max_length=50, blank=False)
    dob = models.DateField(blank=False)
    parent = models.ForeignKey(
        'account.ParentUser', related_name='children', on_delete=models.CASCADE, blank=True, null=True)
    weight = models.FloatField(blank=False)

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

    class Meta:
        ordering = ['-pk']

    def __str__(self):
        return f'{self.name}-{self.child}'


class Reminder(models.Model):

    parent = models.ForeignKey(
        'account.ParentUser', related_name="reminders", on_delete=models.CASCADE)
    vaccine = models.ForeignKey(
        'parent.Vaccine', related_name='reminders', on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return f'{self.parent} {self.date}'


class ReminderANM(models.Model):

    user = models.ForeignKey(
        'account.ANMUser', related_name='reminders_anm', on_delete=models.CASCADE)

    vaccine = models.ForeignKey(
        'parent.Vaccine', related_name='reminders_anm', on_delete=models.CASCADE)
    child = models.ForeignKey(
        'parent.Child', related_name="reminders_anm", on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return f'{self.child} {self.date}'


class AEFI(models.Model):
    child = models.ForeignKey(
        'parent.Child', related_name='AEFIs', on_delete=models.CASCADE)
    vaccine = models.CharField(max_length=100)
    pain = models.BooleanField()
    swelling = models.BooleanField()
    redness = models.BooleanField()
    fever = models.BooleanField()
    irritability = models.BooleanField()
    malaise = models.BooleanField()
    crying = models.BooleanField()

    def __str__(self):
        return self.child.name
