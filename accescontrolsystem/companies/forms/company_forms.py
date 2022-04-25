"""Company forms"""
# Django
import django.forms as forms


# Models
from companies.models import Company
from users.models import User


# Utils
from utils.email import *


# Python
import threading



class CreateCompanyForm(forms.ModelForm):
    """Create form"""

    class Meta:
        model = Company
        fields = '__all__'

    
    def save(self):
        """Create Company."""
        data = self.cleaned_data
        if data['administrator']:
            user = User.objects.get(pk = data['administrator'].pk)
            user.role = 'administrator'
            user.save()
            thread = threading.Thread(target=send_user_mail, 
                                    args= (user,'Assignment to company',
                                    'emails/assignment_to_company.html', 
                                    {'company':data['name'],'operation':'assignment to company'}, ))
            thread.start()

        company = Company.objects.create(**data)

        if data['administrator']:
            user.company = company
            user.save()

        
class UpdateCompanyForm(forms.ModelForm):
    """Create form"""

    class Meta:
        model = Company
        fields = '__all__'

    def save(self,**kwargs):
        """Update Company."""
        data = self.cleaned_data
        if data['administrator']:
            if kwargs.get('pk',False):
                company = Company.objects.get(pk = kwargs['pk'])
                user = User.objects.get(pk = data['administrator'].pk)
                if not company.administrator or company.administrator.pk != user.pk:
                    if company.administrator:
                        last_administrator = company.administrator
                        last_administrator.role = 'user'
                        last_administrator.save()

                        thread = threading.Thread(target=send_user_mail, 
                                    args= (last_administrator,'Admin removal',
                                    'emails/admin_removal.html', {'operation':'admin removal'},))
                        thread.start()
            
                    user.role = 'administrator'
                    user.company = company
                    user.save()
                    thread = threading.Thread(target=send_user_mail, 
                                    args= (user,'Assignment to company',
                                    'emails/assignment_to_company.html', 
                                    {'company':data['name'],'operation':'assignment to company'}, ))
                    thread.start()
    
        else:
            if kwargs.get('administrator',False):
                administrator = kwargs['administrator']
                administrator.role = 'user'
                thread = threading.Thread(target=send_user_mail, 
                                    args= (administrator,'Admin removal',
                                    'emails/admin_removal.html', {'operation':'admin removal'},))
                thread.start()
                administrator.save()

        if kwargs.get('pk',False):
            company = Company.objects.filter(pk = kwargs['pk'])
            company.update(**data)
    

 

