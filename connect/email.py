#The 'EmailMultiAlternatives' class will be responsible for sending the emails
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

# Create an email function that takes in a username and a receiver email
def send_welcome_email(username,receiver):
    # Creating message subject and sender
    subject = 'Welcome to the Connect'
    sender = 'shalyne.waweru@student.moringaschool.com'

    #passing in the context vairables
    text_content = render_to_string('email/welcome.txt',{"username": username})
    html_content = render_to_string('email/welcome.html',{"username": username})

    # Create the EmailMultiAlternativesobject and pass in the subject, the text email template the sender and the receiver.
    msg = EmailMultiAlternatives(subject,text_content,sender,[receiver])
    msg.attach_alternative(html_content,'text/html')
    msg.send()
