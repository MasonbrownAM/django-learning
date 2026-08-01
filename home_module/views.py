from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

# Create your views here.
class HomeView(TemplateView):
    template_name = 'home_module/index_page.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['site_title'] = 'Home'
        return context

def site_header_partial(request):
    return render(request, 'shared/site_header_partial.html',{})

def site_footer_partial(request):
    return render(request, 'shared/site_footer_partial.html',{})