from django.shortcuts import render, redirect
from django.urls import reverse
# Create your views here.
def contact_us(request):
    if request.method == 'POST':
        print(request.POST)
        print(request.POST['email'])
        return redirect(reverse('home'))
    return render(request, 'contact_module/contact_us.html',{})
