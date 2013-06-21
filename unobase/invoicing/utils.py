'''
Created on 06 Jun 2013

@author: michael
'''

from django.conf import settings
from django.core.mail import get_connection, EmailMultiAlternatives
from django.template.loader import render_to_string
from django import http
from django.contrib.sites.models import Site

from unobase.email_tracking import models as email_tracker_models

def send_mail(template_name, context, subject, text_content, from_address, to_addresses, attachments=None, html_content=None, user=None):
    """
    Sends an email containing both text(provided) and html(produced from
    povided template name and context) content as well as provided
    attachments to provided to_addresses from provided from_address.
    """
    if settings.EMAIL_ENABLED:
        # Build message with text_message as default content.
        msg = EmailMultiAlternatives(
            subject,
            text_content,
            from_address,
            to_addresses,
        )
    
        # Set html content from message for HTML capable clients.
        context.update({
            'STATIC_URL': settings.STATIC_URL,
            'site' : Site.objects.get_current()
        })
    
        if template_name is not None:
            html_content = render_to_string(
                template_name,
                context,
            )
    
        if html_content is not None:
            msg.attach_alternative(html_content, "text/html")
    
        # Add attachments.
        if attachments:
            for attachment in attachments:
                if attachment:
                    msg.attach(attachment['name'], attachment['file'].getvalue(), attachment['type'])
    
        # Send message.
        connection = get_connection()
        connection.send_messages([msg, ])
    
        if user is not None:
            email_tracker_models.OutboundEmail.objects.create(user=user, subject=subject, message=html_content)