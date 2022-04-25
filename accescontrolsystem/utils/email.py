# Django
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template



def send_user_mail(user_to_send,subject,template,kwargs):
    template = get_template(template)
    data = {
            'full_name' : user_to_send.first_name + ' ' + user_to_send.last_name,
            }
    if kwargs['operation'] == 'notification registration':
        data['password'] = kwargs['password']
        data['email'] = user_to_send.email

    if kwargs['operation'] == 'assignment to company':
        data['company'] = kwargs['company']

    content = template.render(data)

    message = EmailMultiAlternatives(subject,
                                    "",
                                    settings.EMAIL_HOST_USER,
                                    [user_to_send.email]) 

    message.attach_alternative(content, 'text/html')
    message.send()




