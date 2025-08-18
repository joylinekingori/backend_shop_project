from django.shortcuts import render
from .models import Product
def list_products(request):
   products=Product.objects.all()
   return render(request, "catalogue/products.html",{"products":products})
def product_detail(request,id):
   product=Product.objects.get(id=id)
   return render(request, "catalogue/product_details.html", {"product": product})
from django.shortcuts import render, redirect, get_object_or_404
from .models import Product

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'product_detail.html', {'product': product})

def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart = request.session.get('cart', {})
    
    cart[str(product_id)] = {
        'name': product.name,
        'price': str(product.price),
        'quantity': cart.get(str(product_id), {}).get('quantity', 0) + 1
    }
    
    request.session['cart'] = cart
    return redirect('cart_detail')

def cart_detail(request):
    cart = request.session.get('cart', {})
    cart_items = []
    total = 0
    
    for product_id, item in cart.items():
        product = get_object_or_404(Product, id=product_id)
        quantity = item['quantity']
        subtotal = product.price * quantity
        total += subtotal
        
        cart_items.append({
            'product': product,
            'quantity': quantity,
            'subtotal': subtotal
        })
    
    return render(request, 'cart_detail.html', {
        'cart_items': cart_items,
        'total': total
    })

def remove_from_cart(request, product_id):
    cart = request.session.get('cart', {})
    if str(product_id) in cart:
        del cart[str(product_id)]
        request.session['cart'] = cart
    return redirect('cart_detail')