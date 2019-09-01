from django.db import models


class District(models.Model):
    district_id = models.PositiveIntegerField(blank=False)
    district_inspector_name = models.CharField(max_length=50, blank=False)
    district_inspector_phone = models.PositiveIntegerField(blank=False)
    district_inspector_email = models.EmailField()
    lat = models.CharField(max_length=20)
    lng = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.district_id}'


class Cluster(models.Model):
    district = models.ForeignKey(
        'location.District', related_name='clusters', on_delete=models.CASCADE)
    cluster_id = models.PositiveIntegerField(blank=False)
    cluster_inspector_name = models.CharField(max_length=50, blank=False)
    cluster_inspector_phone = models.PositiveIntegerField(blank=False)
    cluster_inspector_email = models.EmailField()
    lat = models.CharField(max_length=20)
    lng = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.cluster_id}'


class Ward(models.Model):
    cluster = models.ForeignKey(
        'location.Cluster', related_name='wards', on_delete=models.CASCADE)
    ward_id = models.PositiveIntegerField(blank=False)
    ward_inspector_name = models.CharField(max_length=50, blank=False)
    ward_inspector_phone = models.PositiveIntegerField(blank=False)
    ward_inspector_email = models.EmailField()
    lat = models.CharField(max_length=20)
    lng = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.ward_id}'


class Locality(models.Model):
    ward = models.ForeignKey(
        'location.Ward', related_name='localities', on_delete=models.CASCADE)
    locality_id = models.PositiveIntegerField(blank=False)
    name = models.CharField(max_length=50, blank=False)
    locality_inspector_name = models.CharField(max_length=50, blank=False)
    locality_inspector_phone = models.PositiveIntegerField(blank=False)
    locality_inspector_email = models.EmailField()
    lat = models.CharField(max_length=20)
    lng = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.name}'


class Hosptial(models.Model):
    name = models.CharField(max_length=50, blank=False)
    lat = models.CharField(max_length=20, blank=False)
    lng = models.CharField(max_length=20, blank=False)

    def __str__(self):
        return self.name
