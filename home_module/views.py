
from django.shortcuts import render
from django.views.generic import TemplateView
from site_module.models import SiteSettings, FooterLinkBox, Slider


# Create your views here.

# Create your views here.
class HomeView(TemplateView):
    template_name = 'home_module/index_page.html'
    def get_context_data(self, **kwargs):
        context={
            'sliders':Slider.objects.all(),
        }
        return context

def site_header_partial(request):
    site_settings = SiteSettings.objects.filter(is_main_setting=True).first()
    context = {
        'site_settings': site_settings,
    }
    return render(request, 'shared/site_header_partial.html',context= context)

def site_footer_partial(request):
    site_settings = SiteSettings.objects.filter(is_main_setting=True).first()
    footer_link_boxes = FooterLinkBox.objects.all()
    context = {
        'site_settings': site_settings,
        'footer_link_boxes': footer_link_boxes,
    }
    return render(request, 'shared/site_footer_partial.html',context= context)

class AboutView(TemplateView):
    template_name = 'home_module/about.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['site_setting'] = SiteSettings.objects.filter(is_main_setting=True).first()
        return context