from django import forms
from pkg_resources import require


class ContactForm(forms.Form):
    name = forms.CharField(label='نام',
                           max_length=300,
                           error_messages={'required': 'نام خود را وارد کنید'}
                           )
    email = forms.EmailField(label='ایمیل', widget=forms.EmailInput)
    subject = forms.CharField(label='عنوان', max_length=300)
    text = forms.CharField(label='متن', widget=forms.Textarea)

