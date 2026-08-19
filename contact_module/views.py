from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView
from .forms import ContactModelForm, CreateProfileForm
from .models import ContactUs, userProfile


# Create your views here.
class CreateProfileView(CreateView):
    template_name = 'contact_module/create_profile.html'
    model = userProfile
    fields = '__all__'
    success_url = reverse_lazy('home')
class ContactForm(CreateView):
    model = ContactUs
    form_class = ContactModelForm
    template_name = 'contact_module/contact_us.html'
    success_url = reverse_lazy('home')

class ProfileView(ListView):
    model = userProfile
    template_name = 'contact_module/profie_list.html'
    context_object_name = 'profiles'






# class ContactForm(FormView):
#     template_name = 'contact_module/contact_us.html'
#     form_class = ContactModelForm
#     success_url = reverse_lazy('home')
#     def form_valid(self, form):
#         form.save()
#         return super(ContactForm, self).form_valid(form)
#

# def contact_us(request):
#     contact_form = ContactModelForm(request.POST)
#     if request.method == 'POST':
#         if contact_form.is_valid():
#             contact_form.save()
#             return redirect(reverse('home'))
#     else:# if this is get method
#         contact_form = ContactModelForm()
#     return render(request, 'contact_module/contact_us.html',{
#         'contact_form': contact_form,
#     })
