from django.db import models
from django.contrib import auth
# Create your models here.


class User(auth.models.User, auth.models.PermissionsMixin):

    def __str__(self):
        return self.username


class ParentUser(models.Model):

    user = models.OneToOneField(
        auth.models.User, related_name='parentusers', on_delete=models.CASCADE)
    address = models.ForeignKey(
        'location.Locality', related_name='parents', on_delete=models.CASCADE, blank=True, null=True)
    f_name = models.CharField(max_length=50, blank=True)
    m_name = models.CharField(max_length=50, blank=True)
    f_dob = models.DateField(blank=True, null=True)
    m_dob = models.DateField(blank=True, null=True)

    reminder_days = models.IntegerField(blank=True, null=True)
    reminder_frequency = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.user.username


class ANMUser(models.Model):

    user = models.OneToOneField(
        auth.models.User, related_name='anmusers', on_delete=models.CASCADE)
    locality = models.OneToOneField(
        'location.Locality', related_name='anmuserlocalities', on_delete=models.CASCADE)
    phone = models.PositiveIntegerField()

    def __str__(self):
        return self.user.username


class WardUser(models.Model):

    user = models.OneToOneField(
        auth.models.User, related_name='wardusers', on_delete=models.CASCADE)
    ward = models.OneToOneField(
        'location.Ward', related_name='wardusersward', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class ClusterUser(models.Model):

    user = models.OneToOneField(
        auth.models.User, related_name='clusterusers', on_delete=models.CASCADE)
    cluster = models.OneToOneField(
        'location.Cluster', related_name='clusteruserscluster', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class DistrictUser(models.Model):

    user = models.OneToOneField(
        auth.models.User, related_name='districtusers', on_delete=models.CASCADE)
    district = models.OneToOneField(
        'location.District', related_name='districtusersdistrict', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class OTP(models.Model):

    username = models.PositiveIntegerField(blank=False)
    otp = models.PositiveIntegerField(blank=False)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.username}-{self.otp}'
