from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import FormView
from .forms import ContactModelForm

# Create your views here.
class ContactForm(FormView):
    template_name = 'contact_module/contact_us.html'
    form_class = ContactModelForm
    success_url = reverse_lazy('home')
    def form_valid(self, form):
        form.save()
        return super(ContactForm, self).form_valid(form)


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
