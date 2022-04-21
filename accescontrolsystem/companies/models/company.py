"""Company model"""


# Django
from django.db import models
from django.core.validators import RegexValidator




class Company(models.Model):
    """Company model"""

    website_regex =RegexValidator(
        regex=r'[(http(s)?):\/\/(www\.)?a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_\+.~#?&//=]*)',
        message="Invalid URL"

    )
    
    administrator = models.ForeignKey('users.User',
                                        on_delete=models.SET_NULL,
                                        blank=True,null = True,
                                        related_name='company_administrator')

    nit = models.CharField(max_length = 20)
    name = models.CharField(max_length = 50)
    commercial_address = models.CharField(max_length = 250)
    address = models.CharField(max_length = 250)
    phone = models.CharField(max_length = 15)
    email = models.EmailField()
    website = models.CharField(max_length = 50,validators=[website_regex])
    country = models.CharField(max_length = 50)
    state = models.CharField(max_length = 50)
    city = models.CharField(max_length = 50)
