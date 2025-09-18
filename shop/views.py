from django.shortcuts import render, get_object_or_404
from .models import Product

# Create your views here.
def index(request):
    product_objects = Product.objects.all()

    item_name = request.GET.get('item_name')
    if item_name:
        product_objects = product_objects.filter(name__icontains=item_name)
            
    return render(request, 'shop/index.html', {'product_objects': product_objects})

def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'shop/product_detail.html', {'product': product})