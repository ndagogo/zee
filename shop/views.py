from django.shortcuts import render, get_object_or_404
from .models import Product
from django.core.paginator import Paginator


# Create your views here.
def index(request):
    product_objects = Product.objects.all()


    # Search Functionality# Paginator Code   
    item_name = request.GET.get('item_name')
    if item_name:
        product_objects = product_objects.filter(name__icontains=item_name)

    # Paginator Code
    paginator = Paginator(product_objects, 8)  # Show 8 products per page
    page_number = request.GET.get('page')
    product_objects = paginator.get_page(page_number)
            
    return render(request, 'shop/index.html', {'product_objects': product_objects})

def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'shop/product_detail.html', {'product': product})