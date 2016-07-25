from django.shortcuts import render

from .models import Product

# Create your views here.
def product_list(request):
    products = Product.objects.all()
    return render(request, 'base/product_list.html', {'products': products})

def product_detail(request, pk):
    product = Product.objects.get(pk=pk)
    return render(request, 'base/product_detail.html', {'product': product})
