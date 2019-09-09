from django.shortcuts import render, redirect,get_object_or_404
from .models import ProductInfo
from .filter import ProductFilter
from .forms import ProductCreate, CartAddProductsForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from .cart import Cart


def product_list(request):
    template = 'cart/product_list.html'
    products = ProductInfo.objects.all()
    product_filter = ProductFilter(request.GET, queryset=products)
    context = {'products':product_filter}
    return render(request, template, context)

@login_required(login_url='account:account_login')
def product_create(request):
    template = 'cart/product_create.html'
    product_form = ProductCreate(request.POST or None,
                         request.FILES or None)
    if product_form.is_valid():
        product = product_form.save(commit=False)
        print(product)
        product.save()  
        messages.success(request, "Product successfully added")
        return redirect('cart:product_list')
    context = {'form': product_form}
    return render(request, template, context)



def product_detail(request, product_id):
    template = 'cart/product_detail.html'
    cart_product_form = CartAddProductsForm()
    product = get_object_or_404(ProductInfo, id=product_id)
    context = {'product': product, 'cart_product_form': cart_product_form}
    return render(request, template, context)



@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(ProductInfo, id=product_id)
    form = CartAddProductsForm(request.POST)
    
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,
                quantity=cd['quantity'],
                update_quantity = cd['update'])
    return redirect('cart:cart_detail')


def cart_detail(request):
    template = 'cart/product_cart_detail.html'
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductsForm(initial={'quantity': item['quantity'], 'update': True})
    context = {'cart':cart, 'total_price': cart.get_total_price()}    
    return render(request, template, context)


def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(ProductInfo, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')

    

 

