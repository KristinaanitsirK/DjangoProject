from django.contrib.auth.models import User
from django.core.mail import EmailMultiAlternatives
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Product


@receiver(post_save, sender=Product)
def product_created(instance, created, **kwargs):
    if not created:
        return

    emails = User.objects.filter(
        subscriptions__category=instance.category
    ).values_list('email', flat=True)

    subject = f'News product in category {instance.category}'

    text_content = (
        f'Product: {instance.name}\n'
        f'Price: {instance.price}\n\n'
        f'Product link: http://127.0.0.1:8000{instance.get_absolute_url()}'
    )

    html_content = (
        f'Product: {instance.name}<br>'
        f'Price: {instance.price}<br><br>'
        f'<a href="http://127.0.0.1:8000{instance.get_absolute_url()}">Product link</a>'
    )

    for email in emails:
        msg = EmailMultiAlternatives(subject, text_content, None, [email])
        msg.attach_alternative(html_content, 'text/html')
        msg.send()
