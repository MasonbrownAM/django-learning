from django.shortcuts import render, redirect, reverse
from django.views.generic import View
from account_module.forms import RegisterForm, LoginForm
from .models import User
from django.utils.crypto import get_random_string
from django.http import Http404
from django.contrib.auth import login, logout
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
            user_email = register_form.cleaned_data['email']
            user_password = register_form.cleaned_data.get('password')
            user = User.objects.filter(email__iexact=user_email).first()
            user: bool = User.objects.filter(email__iexact=user_email).exists()# if the user registered before
            if user:
                error_message = 'Email already registered'
                register_form.add_error('email', error_message)
                return render(request, 'account_module/registeration.html', context={
                    'register_form': register_form,
                })
            else:
                '''
                email active code: it's an active code which is encrypted 
                and it can be sent with another function
                '''
                new_user = User(username= user_email,email=user_email, email_active_code= get_random_string(48), is_active=True)
                new_user.set_password(user_password)
                new_user.save()# save
                return redirect(reverse('login')) # redirect to login page
        context = {
            'register_form': register_form,
        }
        return render(request, 'account_module/registeration.html', context=context)


class LoginView(View):
    def get(self, request):
        login_form = LoginForm()
        context = {
            'login_form': login_form,
        }
        return render(request, 'account_module/login.html', context=context)

    def post(self, request):
        login_form = LoginForm(request.POST)

        if login_form.is_valid():
            user_email = login_form.cleaned_data['email']
            user_pass = login_form.cleaned_data['password']
            user = User.objects.filter(email__iexact=user_email).first()# look if the user signed in or not
            if user is not None:# if signed in then->
                is_correct = user.check_password(user_pass)# check the encrypted password

                if not user.is_active:
                    login_form.add_error('email', 'your account is not activated.')
                    return render(request, 'account_module/login.html', {'login_form': login_form})
                else:
                    if is_correct:
                        login(request, user)
                        return redirect(reverse('home'))
                    else:
                        login_form.add_error('email', 'Email or password is incorrect.')
                        return render(request, 'account_module/login.html', {'login_form': login_form})
            else:
                login_form.add_error('email', 'Email or password is incorrect.')
                return render(request, 'account_module/login.html', {'login_form': login_form})

        return render(request, 'account_module/login.html', {'login_form': login_form})





class ActivateView(View):
    def get(self, request, email_active_code):
        user= User.objects.filter(email_active_code__iexact=email_active_code).first()
        if user is not None:
            if not user.is_active:
                user.is_active = True
                user.email_active_code = get_random_string(48)
                user.save()
                # todo: show success message to user
                return redirect(reverse('login'))
            else:
                # todo: your account is activated
                 pass

        raise Http404