from django import forms
from pkg_resources import require


class ContactForm(forms.Form):
    name = forms.CharField(label='نام',
                           max_length=300,
                           error_messages={'required': 'نام خود را وارد کنید',},
                           widget=forms.TextInput(
                               attrs={
                                   'class': 'form-control mt-1 mt-1',
                                   'placeholder':'نام',
                               }
                           )
                           )
    email = forms.EmailField(label='ایمیل', widget=forms.EmailInput(
        attrs={
            'class': 'form-control mt-1',
            'placeholder':'ایمیل'
        }
    ))
    subject = forms.CharField(label='عنوان', max_length=300, widget=forms.TextInput(
        attrs={
            'class': 'form-control mt-1',
            'placeholder': 'عنوان'
        }
    ))
    text = forms.CharField(label='متن', widget=forms.Textarea(
        attrs={
            'class': 'form-control mt-1',
            'placeholder': 'متن'
        }
    ))

