from django.db import models


class Region(models.Model):
    region_name = models.CharField(max_length=255, unique=True, choices=[])

    def __str__(self):
        return self.region_name


class Place(models.Model):
    city = models.CharField(max_length=255)
    value = models.IntegerField(default=0)
    region = models.ForeignKey(Region)

    def __str__(self):
        return self.city
