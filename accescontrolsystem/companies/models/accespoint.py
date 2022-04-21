"""Acces point Model"""

# Django
from django.db import models
from django.core.validators import RegexValidator


class AccesPoint(models.Model):
    """AccesPoint Model"""
    name = models.CharField(max_length = 50)
    address = models.CharField(max_length = 250)
    email = models.EmailField()
    company = models.ForeignKey('companies.Company',
                                related_name = 'accespoints_company',
                                on_delete = models.CASCADE)

    geolocation = models.CharField(max_length = 250)
    is_active = models.BooleanField(default = True)

    def __str__(self):
        return self.name
        