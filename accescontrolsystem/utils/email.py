# Django
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template


def send_user_mail(user_to_send, subject, template, kwargs):
    template = get_template(template)
    data = {
        'full_name': user_to_send.first_name + ' ' + user_to_send.last_name,
    }
    if kwargs['operation'] == 'notification registration':
        data['password'] = kwargs['password']
        data['email'] = user_to_send.email

    if kwargs['operation'] == 'assignment to company' or kwargs['operation'] == 'invitation' or kwargs['operation'] == 'notification registration company':
        data['company'] = kwargs['company']
    
    if kwargs['operation'] == 'unauthorized':
        data['acces_point'] = kwargs['acces_point'][0]
        data['email'] = user_to_send.email
        data['user_not_allowed'] = kwargs['user']

    content = template.render(data)

    message = EmailMultiAlternatives(subject,
                                     "",
                                     settings.EMAIL_HOST_USER,
                                     [user_to_send.email])

    message.attach_alternative(content, 'text/html')
    message.send()
