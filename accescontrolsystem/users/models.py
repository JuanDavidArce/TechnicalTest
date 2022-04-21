"""User model"""

#django
from django.db  import models
from django.contrib.auth.models import AbstractUser




class User(AbstractUser):
    """User model 
    Extend from djangos's abstract user, change the username field 
    to email """
    email = models.EmailField(
        'email_address',
        unique=True,
        error_messages={
            'unique':'A user with that email already exists'
        }
    )
    company = models.ForeignKey('companies.Company',
                                on_delete=models.SET_NULL,
                                blank = True,null = True,
                                related_name='users_company')
    
    address = models.EmailField()
    phone = models.CharField(max_length = 15)
    country = models.CharField(max_length = 50)
    state = models.CharField(max_length = 50)
    city = models.CharField(max_length = 50)
    role = models.CharField(max_length = 50,default='user')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS =['role','first_name','last_name']


    def __str__(self):
        return self.first_name + ' '+ self.last_name

