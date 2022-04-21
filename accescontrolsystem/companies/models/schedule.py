"""Schedule model"""


# Django
from django.db import models
from django.core.validators import RegexValidator


class Schedule(models.Model):
    """Schedule model"""

    acces_point = models.ForeignKey('companies.AccesPoint',
                                    related_name = 'schedules_acces_point',
                                    on_delete = models.CASCADE)

    start_time = models.TimeField()
    ending_time = models.TimeField()
    user = models.ForeignKey('users.User',
                            related_name = 'schedules_user',
                            on_delete = models.CASCADE)
