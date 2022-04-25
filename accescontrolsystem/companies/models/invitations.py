"""Invitation model"""


# Django
from django.db import models


class Invitation(models.Model):
    """Invitation model"""

    company = models.ForeignKey('companies.Company',
                                    related_name = 'invitations_company',
                                    on_delete = models.CASCADE)
    email = models.EmailField(unique=True,
                            error_messages={
                            'unique':'A user with that email already exists'})
    
    pin = models.CharField(max_length = 32,unique=True,null=False,default='None')
