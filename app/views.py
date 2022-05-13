from email import message
from io import BufferedRandom
from itertools import product
from pyexpat.errors import messages
from unicodedata import category
from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.views import View 
from django.contrib.auth import authenticate , login , logout
from .forms import CustomerProfileForm, CustomerRegistrationForm
from .models import Cart , Product , OrderPlaced , Customer
from django.contrib.auth.models import User
from .serializers import CustomerSerializer , ProductSerializer
from rest_framework.renderers import JSONRenderer

# def home(request):
#  return render(request, 'app/home.html')



class CustomerRegistraionView(View):
    def get(self , request):                                                #For Get
        form = CustomerRegistrationForm()
        return render(request , 'app/register.html',{'form':form})

    def post(self,request):                                                 #For Post
        if request.method == "POST":
            form = CustomerRegistrationForm(request.POST)
            if form.is_valid():
                user = form.save()
                login(user)
                return redirect('home')
        context = {'form':form}
        return render(request , 'app/register.html' , context)

class HomeView(View):
    def get(self , request):
        TopWear = Product.objects.filter(category='TW')
        BottomWear = Product.objects.filter(category='BW')
        Laptop = Product.objects.filter(category='L')
        Mobiles = Product.objects.filter(category='M')

        context = {"Mobiles":Mobiles , "BottomWear":BottomWear , "Laptop":Laptop , "TopWear":TopWear}
        return render(request , 'app/home.html' , context)


# def product_detail(request):
#  return render(request, 'app/productdetail.html')

class ProductDetailView(View):
    def get(self , request , pk):
        product = Product.objects.get(pk=pk)

        context = {"product":product}
        return render(request , 'app/productdetail.html' , context)

def add_to_cart(request):
    user = request.user
    product_id = request.GET.get('prod_id')
    print(product_id)
    product = Product.objects.get(id=product_id)
    Cart(user=user , product=product).save()
    # context = {'user':user , 'product_id':product_id , 'product':product}
    # return render(request , 'app/addtocart.html')
    return redirect('cart')

def showcart(request):
    if request.user.is_authenticated:
        user = request.user
        cart = Cart.objects.filter(user=user)
        amount = 0.0
        shipping_charge = 80.0
        total_amount = 0.0
        cart_product= [p for p in Cart.objects.all() if p.user == user]
        
        if cart_product:
            for p in cart_product:
                temamount = (p.quantity * p.product.selling_price)
                amount += temamount 
                total_amount = amount + shipping_charge
            context = {'cart':cart , "totalAmount":total_amount}
            return render(request , 'app/addtocart.html' , context)
        else:
            return HttpResponse("No cart in your Account")

def buy_now(request):
 return render(request, 'app/buynow.html')

# def profile(request):
#  return render(request, 'app/profile.html')

def address(request):
    customer = Customer.objects.filter(user = request.user)
    context = {'customer':customer ,'active': 'btn-primary'}
    return render(request, 'app/address.html',context)

def orders(request):
 return render(request, 'app/orders.html')

def change_password(request):
 return render(request, 'app/changepassword.html')

def MobileView(request , data=None):

    if data == None:
        mobiles = Product.objects.filter(category="M")
    elif data == "Apple":
        mobiles = Product.objects.filter(category="M").filter(brand="Apple")
    elif data == "Oppo":
        mobiles = Product.objects.filter(category="M").filter(brand="Oppo")
    elif data == "Oneplus":
        mobiles = Product.objects.filter(category="M").filter(brand="Oneplus")
    elif data == "Above":
        mobiles = Product.objects.filter(category="M").filter(discounted_price__gt=60000)
    elif data == "Below":
        mobiles = Product.objects.filter(category="M").filter(discounted_price__lt=60000)
    else : 
        mobiles = Product.objects.filter(category="M")
    
    context = {"mobiles":mobiles}
    return render(request , 'app/mobile.html' , context)
    

def laptopView(request , data=None):
    
    if data == None:
        laptop = Product.objects.filter(category="L")
    elif data == "Apple":
        laptop = Product.objects.filter(category="L").filter(brand="Apple")
    elif data == "Lenevo":
        laptop = Product.objects.filter(category="L").filter(brand = "Lenevo")
    elif data == "Reamle":
        laptop = Product.objects.filter(category="L").filter(brand="Realme")
    elif data == "Samsung":
        laptop = Product.objects.filter(category="L").filter(brand="Samsung")
    elif data == "Above":
        laptop = Product.objects.filter(category="L").filter(selling_price__gt=80000)
    elif data == "Below":
        laptop = Product.objects.filter(category="L").filter(selling_price__lt=80000)
    
    context = {"laptops":laptop}
    return render(request , 'app/laptop.html' , context)


def login(request):
 return render(request, 'app/login.html')

def customerregistration(request):
 return render(request, 'app/customerregistration.html')

def checkout(request):
 return render(request, 'app/checkout.html')

def Bottom_wear(request , data = None):
    
    if data == None:
        bottomWear = Product.objects.filter(category="BW")
    elif data == "Laira":
        bottomWear = Product.objects.filter(category="BW").filter(brand="Laira")
    elif data == "Nike":
        bottomWear = Product.objects.filter(category="BW").filter(brand="Nike")
    elif data == "Zara":
        bottomWear = Product.objects.filter(category="BW").filter(brand="Zara")
    elif data == "Levis":
        bottomWear = Product.objects.filter(category="BW").filter(brand="Levis")
    else:
        bottomWear = Product.objects.filter(category="BW")
    
    context = {'bottomWear':bottomWear}
    return render(request , 'app/bottomwear.html' , context)


#For API 
def Customer_detail(request , pk):
    customer = Customer.objects.get(id=pk)
    serial = CustomerSerializer(customer)
    json_data = JSONRenderer().render(serial.data)
    return HttpResponse(json_data , 'application/json')


def Customer_detailAll(request):
    customers = Customer.objects.all()
    serials = CustomerSerializer(customers , many=True)
    json_data = JSONRenderer().render(serials)
    return HttpResponse(json_data , 'application/json')

def Product_detailapi(request):
    product = Product.objects.all()
    serial = ProductSerializer(product , many=True)
    json_data = JSONRenderer().render(serial.data)
    return HttpResponse(json_data , 'application/json')

class ProfileView(View):
    def get(self , request):        # Get view
        form = CustomerProfileForm()
        context = {'form':form , 'activecss':'btn-primary'}
        return render(request , 'app/profile.html' , context)

    def post(self , request): # POST view
        form = CustomerProfileForm(request.POST)
        if form.is_valid(): 
            P_user = request.user
            name = form.cleaned_data['name']                            #  Form cleaning
            locality = form.cleaned_data['locality']
            city = form.cleaned_data['city']
            zipcode = form.cleaned_data['zipcode']
            state = form.cleaned_data['state']

            Pdata = Customer(user=P_user,name=name , locality=locality , city=city , zipcode=zipcode , state=state)
            Pdata.save()

            context = {'form':form}
            return render(request , 'app/profile.html' , context)
        else:
            return HttpResponse("Your request is invalid!")

        
