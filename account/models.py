from django.db import models
from django.contrib import auth
# Create your models here.


class User(auth.models.User, auth.models.PermissionsMixin):

    def __str__(self):
        return self.username


class ParentUser(models.Model):

    user = models.ForeignKey(
        auth.models.User, related_name='parentusers', on_delete=models.CASCADE)
    address = models.TextField(blank=True)
    f_name = models.CharField(max_length=50, blank=True)
    m_name = models.CharField(max_length=50, blank=True)
    f_dob = models.DateField(blank=True, null=True)
    m_dob = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.user.username


class ANMUser(models.Model):

    user = models.ForeignKey(
        auth.models.User, related_name='anmusers', on_delete=models.CASCADE)
    locality = models.ForeignKey(
        'location.Locality', related_name='anmuserlocalities', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class WardUser(models.Model):

    user = models.ForeignKey(
        auth.models.User, related_name='wardusers', on_delete=models.CASCADE)
    ward = models.ForeignKey(
        'location.Ward', related_name='wardusersward', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class ClusterUser(models.Model):

    user = models.ForeignKey(
        auth.models.User, related_name='clusterusers', on_delete=models.CASCADE)
    cluster = models.ForeignKey(
        'location.Cluster', related_name='clusteruserscluster', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class OTP(models.Model):

    username = models.PositiveIntegerField(blank=False)
    otp = models.PositiveIntegerField(blank=False)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.username}-{self.otp}'
