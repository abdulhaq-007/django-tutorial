from django.shortcuts import render
from django.views.generic.base import View
# Create your views here.
from .models import Product

class HopePageView(View):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        popular = Product.objects.filter(top=True)
        discount = Product.objects.filter(discount__gte=0)

        data = {
            "popular_products":popular,
            "discount_products":discount
        }
        return render(request, self.template_name)

