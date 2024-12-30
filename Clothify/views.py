from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Products, Category, Cart, Order

# Create your views here.
def home(request):
    products = Products.objects.all()
    return render(request, 'index.html', {"products":products})

def auth(request):
    return render(request, 'auth.html', {})

def signup(request):
    if request.method == 'POST':
        username =  request.POST['email']
        password = request.POST['password']
        full_name = request.POST['full_name']

        first_name = full_name.split(' ')[0]
        last_name = full_name.split(' ')[1]

        users = User.objects.create_user(username=username, password=password, email=username, first_name=first_name, last_name=last_name)

        print("User created Successfully !!!", users)

        return redirect('/')
    
#  login function
def signin(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        # login 
        user = authenticate( request,username=email, password=password)
        if user is not None:
            login(request, user)
            print("User logged In", user)
            return redirect('/')
        else:
            print("Invalid Credentials!!")
            return redirect('/auth')
        
def sign_out(request):
    logout(request)
    return redirect('/')
        

def product_details(request, id):
    product = Products.objects.get(id = id)
    return render(request, 'product-detail.html', {"product":product})

def product_list(request):
    products = Products.objects.all()
    categories = Category.objects.all()
    return render(request, 'product-list.html', {'products': products, 'categories':categories})


def category_product_list(request, category):
    products = Products.objects.filter(category__name=category)
    categories = Category.objects.all()
    return render(request, 'product-list.html', {'products': products, 'categories':categories})


def cart(request):
    if request.user.is_authenticated:
        cart = Cart.objects.get(user = request.user)
        cart_items = cart.product.all()
        grand_sum = 0 
        for item in cart_items:
            grand_sum+=item.price
        return render(request, 'cart.html', {"cart_items":cart_items, "grand_sum":grand_sum})
    else:
        print('User not logged in')
        return redirect('/auth')

def add_to_cart(request, product_id):
    if request.user.is_authenticated:
        try:
            existing_cart = Cart.objects.get(user=request.user)
            if existing_cart:
                # add product to that cart
                existing_cart.product.add(product_id)
                print(f"Product {product_id} is added to the Cart!!")
            else:
                # user does not have any cart yet
                # Create Cart
                new_cart = Cart.objects.create(user= request.user)
                # Add product to the cart
                new_cart.product.add(product_id)
                print(f"Product {product_id} is added to the Cart!!")


        except Cart.DoesNotExist:
            # user does not have any cart yet
            # Create Cart
            new_cart = Cart.objects.create(user= request.user)
            # Add product to the cart
            new_cart.product.add(product_id)
            print(f"Product {product_id} is added to the Cart!!")

    else:
        print("User is not logged in")

    return redirect('/')

def delete_cart_item(request, product_id):
    cart = Cart.objects.get(user= request.user)
    cart.product.remove(product_id)
    print("Item deleted from Cart!")
    return redirect('/cart')

from uuid import uuid4
def checkout(request):
    cart = Cart.objects.get(user = request.user)
    cart_items = cart.product.all()
    grand_sum = 0 
    for item in cart_items:
        grand_sum+=item.price
    
    # if method is post i.e. Checkout
    if request.method =="POST":
        # create order
        order_id = str(uuid4())
        address = request.POST['address']
        mobile_no = request.POST['mobile_no']

        for item in cart_items:
            Order.objects.create(order_id=order_id,user= request.user, product = item, address =address, mobile_no=mobile_no)
            # remove ordered product from cart
            cart.product.remove(item)
            
        print("Order Placed!!")
        return redirect('/')


    return render(request, 'checkout.html', {'cart_items':cart_items, 'grand_sum':grand_sum})


def orders(request):
    orders = Order.objects.filter(user= request.user).order_by('order_id')

    order_list=[]

    temp_order_id = ''
    total_order_price=0
    for order in orders:
        if temp_order_id != order.order_id:
            temp_order_id = order.order_id
            order_list.append({"order_id":order.order_id, 'order_price':total_order_price, 'status':order.status})
        else:
            total_order_price+= order.product.price
            order_list[-1] = {"order_id":order.order_id, 'order_price':total_order_price, 'status':order.status}

    return render(request, 'orders.html', {"order_list":order_list, "orders":orders})