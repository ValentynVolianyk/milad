from django.shortcuts import get_list_or_404
from django.views.generic import TemplateView, DetailView
from django.http import HttpResponse
from django.template.response import TemplateResponse
from .models import Category, Product, Size
from django.db.models import Q

class IndexViev(TemplateView):
    template_name = 'main/base.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['current_category'] = None
        return context
    
    def get(self, request, *args, **kwargs):
        contex = self.get_context_data(**kwargs)
        if request.headers.get('HX-Request'):
            return TemplateResponse(request, 'main/home_content.html', contex)
        return TemplateResponse(request, self.template_name,contex )
    
class CatalogView(TemplateView):
    template = 'main/base.html'

    FILTER_MAPPING = {
        'color': lambda queryset, value: queryset.filter(color__iexact=value),
        'min_price': lambda queryset, value: queryset.filter(price_gte=value),
        'max_price': lambda queryset, value: queryset.filter(price_lte=value),
        'size': lambda queryset, value: queryset.filter(product_sizes__name=value),
    }

