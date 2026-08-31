from symtable import Class
from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth import get_user_model
from account_module.forms import RegisterForm

User = get_user_model()
# Create your views here.
class RegisterView(View):
    def get(self, request):
        register_form = RegisterForm()
        context = {
            'register_form': register_form,
        }
        return render(request, 'account_module/registeration.html', context=context)

    def post(self, request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            print(register_form.cleaned_data)
            # todo: register user
            pass
        context = {
            'register_form': register_form,
        }
        return render(request, 'account_module/registeration.html', context=context)


