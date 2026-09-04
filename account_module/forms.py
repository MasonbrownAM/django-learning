from xml.dom import VALIDATION_ERR

from django import forms
'''
در انجا میخواهیم از validator ها استفاده کنیم و ببینیم چطور کار میکنن 
در واقع این کتابخانه بشما کمک میکند محدودیت داخل فرم هایتان ایجاد بکنید
'''
from django.core import validators
from django.core.exceptions import ValidationError


class RegisterForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(),
        label = 'ایمیل',
        validators=
        [
            validators.MaxLengthValidator(100),
            validators.EmailValidator()
        ]
    )
    password = forms.CharField(
        label='رمز',
        widget=forms.PasswordInput(),
        validators=[
            validators.MaxLengthValidator(100),
            validators.EmailValidator()
        ]
    )
    password_confirm = forms.CharField(
        widget=forms.PasswordInput(),
        label='رمز دوباره'
    )
    '''
    میتوانید validator های دلخواخ خود را بسازید 
    1. clean_FormDataName()
    2. Get the data
    3. Conditions
    '''
    def clean_password_confirm(self):
        password = self.cleaned_data.get('password')
        password_confirm = self.cleaned_data.get('password_confirm')
        if password != password_confirm:
            raise ValidationError('رمز یکی نیست!')
        else:
            return password_confirm


class LoginForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(),
        label = 'ایمیل',
        validators=
        [
            validators.MaxLengthValidator(100),
            validators.EmailValidator()
        ]
    )
    password = forms.CharField(
        label='رمز',
        widget=forms.PasswordInput(),
        validators=[
            validators.MaxLengthValidator(100),
            validators.EmailValidator()
        ]
    )
