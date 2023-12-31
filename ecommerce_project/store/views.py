import json
import datetime
from .models import *
from .utils import cookieCart, cartData, guestOrder
from django.shortcuts import render
from django.http import JsonResponse


# Create your views here.
def store(request):

    data = cartData(request)
    cartItems = data['cartItems']
    products = Product.objects.all()

    context = {'products': products, 'cartItems': cartItems}
    return render(request, 'store/store.html', context)

def cart(request):

    data = cartData(request)
    items = data['items']
    order = data['order']
    cartItems = data['cartItems']

    context = {'items': items, 'order': order, 'cartItems': cartItems}
    return render(request, 'store/cart.html', context)

def checkout(request):

    data = cartData(request)
    items = data['items']
    order = data['order']
    cartItems = data['cartItems']

    context = {'items': items, 'order': order, 'cartItems': cartItems}
    return render(request, 'store/checkout.html', context)

def productDetail(request, id):
    """Description for product detail"""
    data = cartData(request)
    cartItems = data['cartItems']
    product = Product.objects.get(id=id)
    context = {'product': product, 'cartItems': cartItems}
    return render(request, 'store/productDetail.html', context)

def updateItem(request):
    """Business logic for updating an item"""
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)

    orderItem, created = OrderItem.objects.get_or_create(product=product, order=order)

    if action == 'add':
        orderItem.quantity += 1
    elif action == 'remove':
        orderItem.quantity -= 1

    orderItem.save()
    
    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse('Item was added', safe=False)

def processOrder(request):
    """Generate a transaction Id and update the order status"""
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
    else:
        customer, order = guestOrder(request, data)
    
    total = float(data['form']['total'])
    order.transaction_id = transaction_id

    if total == float(order.get_cart_total):
        order.complete = True
    order.save()

    if order.shipping == True:
        ShippingAddress.objects.create(
            customer=customer,
            order=order,
            address=data['shipping']['address'],
            city=data['shipping']['city'],
            state=data['shipping']['state'],
            zipcode=data['shipping']['zipcode']
        )
    return JsonResponse('Order was complete!', safe=False)
