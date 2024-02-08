from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.urls import reverse


def send_test(request, username, email_address):
    email = EmailMultiAlternatives()
    email.subject = "This is a test"
    email.from_email = "jefvanrompay@gmail.com"
    email.to = [email_address]

    link_url = request.build_absolute_uri(reverse('mails:send_mail'))

    context = {
        'username' : username,
        'email_address' : email_address,
        'link_url' : link_url,
    }

    html_content = render_to_string('emailing/emails/test.html', context)
    email.attach_alternative(html_content, 'text/html')
    email.send(fail_silently=False)





# def integrate_sendgrid():
#     # using SendGrid's Python Library
#     # https://github.com/sendgrid/sendgrid-python
#     import os
#     from sendgrid import SendGridAPIClient
#     from sendgrid.helpers.mail import Mail

#     message = Mail(
#         from_email='from_email@example.com',
#         to_emails='jefvanrompay@gmail.com',
#         subject='Sending with Twilio SendGrid is Fun',
#         html_content='<strong>and easy to do anywhere, even with Python</strong>')
#     try:
#         sg = SendGridAPIClient('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')
#         response = sg.send(message)
#         print(response.status_code)
#         print(response.body)
#         print(response.headers)
#     except Exception as e:
#         print(e)