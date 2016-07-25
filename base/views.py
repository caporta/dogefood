from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required

from .models import Product


# Create your views here.
@login_required(login_url='/login/')
def product_list(request):
    products = Product.objects.all()
    return render(request, 'base/product_list.html', {'products': products})


@login_required(login_url='/login/')
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'base/product_detail.html', {'product': product})
