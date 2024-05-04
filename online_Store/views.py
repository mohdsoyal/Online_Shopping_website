from django.shortcuts import render,redirect
from .models import Product,Custumer,Cart,Orderplaced
from .forms import CustomerRegistrationForm ,UserloginForm,CustumerForm
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from django.db.models import Q
from django.http import JsonResponse



def home(request):
  topwear=Product.objects.filter(category='TW').order_by("?")
  bottomwear=Product.objects.filter(category='BW').order_by("?")
  mobiles=Product.objects.filter(category='M').order_by("?")
  laptop=Product.objects.filter(category='L').order_by("?")
  return render(request, 'home.html',{'topwear':topwear,'bottomwear':bottomwear,'mobiles':mobiles,'laptop':laptop})


# single_page.................
def product_detail(request, id):
    product = Product.objects.get(id=id)
   
    if request.user.is_authenticated:
        # Check if the item is already in the cart
        item_already_in_cart = Cart.objects.filter(product=product, user=request.user).exists()
    else:
        item_already_in_cart = False

    return render(request, 'productdetail.html', {'product': product, 'already': item_already_in_cart})


#show the admin user add to cart item.........
@login_required(login_url='login')
def add_to_cart(request):
 user=request.user
 product_id=request.GET.get('prod_id')
 product =Product.objects.get(id=product_id)
 Cart(user=user,product=product).save()
 return redirect('/Cart')

#show the Template........
@login_required(login_url='login')
def showcart(request):
    user = request.user
    cart = Cart.objects.filter(user=user)
    #amount calculation process........
    amount = 0.0
    shopping_amount = 70
    total_amount = 0.0
    for cart_item in cart:
        temp_amount = cart_item.quantity * cart_item.product.selling_price
        amount += temp_amount
    total_amount = amount + shopping_amount
    return render(request, 'addtocart.html', {'carts': cart, 'total_amount': total_amount, 'amount': amount})

# Cart QTY Plus.............................
@login_required(login_url='login')
def pluscart(request):
    if request.method == 'GET':
        prod_id = request.GET.get('prod_id')
        cart_item = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        cart_item.quantity += 1
        cart_item.save()
        amount = cart_item.quantity * cart_item.product.selling_price
        shopping_amount = 70
        total_amount = amount + shopping_amount

        data = {
            'quantity': cart_item.quantity,
            'amount': amount,
            'total_amount': total_amount,
        }

        return JsonResponse(data)
    
#  Cart QTY Minus.................... 
@login_required(login_url='login')  
def minuscart(request):
    if request.method == 'GET':
        prod_id = request.GET.get('prod_id')
        cart_item = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        cart_item.quantity -= 1
        cart_item.save()

        amount = cart_item.quantity * cart_item.product.selling_price
        shopping_amount = 70
        total_amount = amount + shopping_amount

        data = {
            'quantity': cart_item.quantity,
            'amount': amount,
            'total_amount': total_amount,
        }

        return JsonResponse(data)    

# Remove the Cart QTY.....................
@login_required(login_url='login')
def removecart(request):
    if request.method == 'GET':
        prod_id = request.GET.get('prod_id')
        cart_item = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        cart_item.delete()

        amount = cart_item.quantity * cart_item.product.discount_price
        shopping_amount = 70
        total_amount = amount + shopping_amount

        data = {
            
            'amount': amount,
            'total_amount': total_amount,
        }

        return JsonResponse(data)    
 
 

def buy_now(request):
 return render(request, 'buynow.html')

# User Address Page.............
@login_required(login_url='login')
def address(request):
 address=Custumer.objects.filter(user=request.user)
 return render(request, 'address.html',{'address':address})

# Order Page..............................
def orders(request):
 user=request.user
 op = Orderplaced.objects.filter(user=request.user)
 cart_item = Orderplaced.objects.filter(user=user,status='Pending').count()
 return render(request, 'orders.html',{'op':op,'cart_item':cart_item})

# Password Change.............................
@login_required(login_url='login')
def change_password(request):
 return render(request, 'changepassword.html')


# Check The Mobile Category.......................
def mobile(request, data=None):
    if data is None:
        mobiles = Product.objects.filter(category='M').order_by("?")
    elif data == 'Redmi':
        mobiles = Product.objects.filter(category='M', brand=data).order_by("?")
    elif data == 'Sumsung':
        mobiles = Product.objects.filter(category='M', brand=data).order_by("?")    
    elif data == 'Oppo':
        mobiles = Product.objects.filter(category='M', brand=data).order_by("?")        
    elif data == 'below':
        mobiles = Product.objects.filter(category='M').filter(discount_price__lt=10000)
    elif data == 'above':
        mobiles = Product.objects.filter(category='M').filter(discount_price__gt=10000)     
    else:
        mobiles = []
    return render(request, 'mobile.html', {'mobiles': mobiles})


# Check The Mobile Category.......................
def laptops(request,data=None):
    if data is None:
        laptop = Product.objects.filter(category='L').order_by("?")
    elif data == 'Dell':
        laptop = Product.objects.filter(category='L', brand=data).order_by("?")
    elif data == 'HP':
       laptop = Product.objects.filter(category='L', brand=data).order_by("?")   
    elif data == 'Lenovo':
        laptop = Product.objects.filter(category='L', brand=data).order_by("?")        
    elif data == 'below':
       laptop = Product.objects.filter(category='L').filter(discount_price__lt=50000)
    elif data == 'above':
       laptop = Product.objects.filter(category='L').filter(discount_price__gt=50000)     
    else:
        laptop = []
    return render(request,'laptop.html',{'laptop':laptop})

def top(request,data=None):
    if data is None:
        topwear = Product.objects.filter(category='TW').order_by("?")
    elif data == 'T-Shirt':
        topwear = Product.objects.filter(category='TW', brand=data).order_by("?")
    elif data == 'Shirt':
        topwear = Product.objects.filter(category='TW', brand=data).order_by("?")    
    elif data == 'Oppo':
       topwear = Product.objects.filter(category='TW', brand=data).order_by("?")        
    elif data == 'below':
        topwear = Product.objects.filter(category='TW').filter(discount_price__lt=2000)
    elif data == 'above':
        topwear = Product.objects.filter(category='TW').filter(discount_price__gt=2000)     
    else:
        topwear = []
    return render(request,'top.html',{'topwears':topwear})


def bottom(request,data=None):
    if data is None:
        bottomwear = Product.objects.filter(category='BW').order_by("?")
    elif data == 'T-Shirt':
        bottomwear = Product.objects.filter(category='BW', brand=data).order_by("?")
    elif data == 'Shirt':
        bottomwear = Product.objects.filter(category='BW', brand=data).order_by("?")    
    elif data == 'Oppo':
      bottomwear = Product.objects.filter(category='BW', brand=data).order_by("?")        
    elif data == 'below':
        bottomwear = Product.objects.filter(category='BW').filter(discount_price__lt=2000)
    elif data == 'above':
        bottomwear = Product.objects.filter(category='BW').filter(discount_price__gt=2000)     
    else:
        bottomwear = []
    return render(request,'bottom.html',{'bottomwear':bottomwear})



def login_page(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('profile')
    else:
     return render(request,'login.html')


def customerregistration(request):
  if request.method=='POST':
     fm=CustomerRegistrationForm(request.POST)
     if fm.is_valid():
        messages.success(request ,'Congratulations!! Registred Successfully')
        fm.save()
        return redirect('login')
  else:
        fm=CustomerRegistrationForm() 
  return render(request, 'customerregistration.html',{'form':fm})

def logout_page(request):
    logout(request)
    return redirect('/')


@login_required(login_url='login')
def checkout(request):
 user = request.user
 add=Custumer.objects.filter(user=user)
 cart_item = Cart.objects.filter(user=user)
 amount =0
 shipping_amount = 70.0
 totalamount = 0.0
 cart_product =[p for p in Cart.objects.all() if p.user==request.user]
 if cart_product:
     for p in cart_product:
         tempamount = (p.quantity * p.product.selling_price)
         amount += tempamount
         totalamount = amount + shipping_amount
 return render(request, 'checkout.html',{'add':add,'totalamount':totalamount,'cart_item':cart_item})



def paymentdone(request):
    user = request.user
    custid = request.GET.get('custid')
    customer = Custumer.objects.get(id=custid)
    cart = Cart.objects.filter(user=user)
    for c in cart:
        Orderplaced(user=user,customer=customer,product=c.product,quantity=c.quantity).save()
        c.delete()
    return redirect('orders')   




@login_required(login_url='login')
def profile(request):
 form=CustumerForm(request.POST)
 if form.is_valid():
     user =request.user
     name=form.cleaned_data['name']
     locality=form.cleaned_data['locality']
     city=form.cleaned_data['city']
     state=form.cleaned_data['state']
     zipcode=form.cleaned_data['zipcode']
     saved = Custumer(user=user,name=name,locality=locality,city=city,state=state,zipcode=zipcode)
     saved.save()
     messages.success(request ,'Congratulations!! Profile Updated Successfully')
     
 else:
    form=CustumerForm()  
 return render(request, 'profile.html',{'form':form ,'active':'btn-danger'})


# SEarching ......................
def search(request):
    if request.method =='GET':
        st=request.GET.get('search')
        data=Product.objects.filter(brand__icontains=st)
    return render(request,'search.html',{'data':data})
