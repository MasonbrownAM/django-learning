from django.shortcuts import render
# Create your views here.
def contact_us(request):
    return render(request, 'contact_module/contact_us.html',{})