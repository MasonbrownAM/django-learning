from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import ContactForm
# Create your views here.
def contact_us(request):
    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            print(contact_form.cleaned_data)
            return redirect(reverse('home'))
    else:# if this is get method
        contact_form = ContactForm()
    return render(request, 'contact_module/contact_us.html',{
        'contact_form': contact_form,
    })
