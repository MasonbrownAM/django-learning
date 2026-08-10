from django import forms
from django.views.generic import CreateView
from pkg_resources import require
from .models import ContactUs
class ContactModelForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ('name', 'email', 'title', 'description')
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control mt-1',
                'placeholder': 'نام'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control mt-1',
                'placeholder': 'ایمیل'
            }),
            'title': forms.TextInput(attrs={
                'class': 'form-control mt-1',
                'placeholder': 'عنوان'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control mt-1',
                'placeholder': 'متن'
            })
        }
        labels = {
            'name': 'نام',
            'email': 'ایمیل',
            'title': 'عنوان',
            'description': 'توضیحات',
        }
        error_messages = {
            'name': {
                'required': 'نام الازمی میباشد'
            },
            'email': {
                'required': 'ایمیل الزامی میباشد'
            },
            'title': {
                'required': 'عنوان الزامی میباشد'
            },
            'description': {
                'required' : 'توضیحات الزامی'
            }
        }
        # fields = '__all__'
        # exclude = ('id',)

class CreateProfileForm(forms.Form):
    user_image = forms.FileField()