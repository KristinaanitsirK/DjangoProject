# from django import forms
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User

from django.contrib.auth.models import Group
from allauth.account.forms import SignupForm
from django.core.mail import EmailMultiAlternatives, mail_managers, mail_admins


# class SignUpForm(UserCreationForm):
#     email = forms.EmailField(label='Email')
#     first_name = forms.CharField(label='Name')
#     last_name = forms.CharField(label='Surname')
#
#     class Meta:
#         model = User
#         fields = (
#             'username',
#             'first_name',
#             'last_name',
#             'email',
#             'password1',
#             'password2',
#         )


class CustomSignupForm(SignupForm):
    def save(self, request):
        user = super().save(request)
        common_users = Group.objects.get(name='common users')
        user.groups.add(common_users)

        subject = 'Welcome to Our e-shop!'
        text = f'{user.username}, you have successfully signed up!'
        html = (
            f'<b>{user.username}</b>, you have successfully signed up on'
            f'<a href="http://127.0.0.1:8000/products"> SImpleAppWebShopSite</a>!'
        )
        msg = EmailMultiAlternatives(
            subject=subject,
            body=text,
            from_email=None,
            to=[user.email],
        )
        msg.attach_alternative(html, 'text/html')
        msg.send()

        mail_managers(
            subject='New User',
            message=f'New user {user.username} has been registered.'
        )

        mail_admins(
            subject='New User',
            message=f'New user {user.username} has been registered on simpleapp website.'
        )

        return user

