from re import template
from django.urls import path
from app import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views
from .forms import MyPasswordChangeForm, UserLoginForm


urlpatterns = [
    path('', views.HomeView.as_view() , name = "home"),
    #authenticate urls :
    path('accounts/login',auth_views.LoginView.as_view(
        template_name = 'app/login.html' , authentication_form = UserLoginForm 
    ) , name='login'),

    path('logout/',auth_views.LogoutView.as_view(next_page ='login') , name='logout'),

    path('passwordchange/',auth_views.PasswordChangeView.as_view(
        template_name= 'app/passwordchange.html' , form_class=MyPasswordChangeForm), name='passwordchange'),
    path('passwordchangedone/',auth_views.PasswordChangeView.as_view(
        template_name= 'app/passwordchange.html'), name='passwordchangedone'),

    path('registration/', views.CustomerRegistraionView.as_view(), name='customerregistration'),
    
    #product urls 
    path('product-detail/<int:pk>/', views.ProductDetailView.as_view(), name='product-detail'),
    path('add-to-cart/' , views.add_to_cart , name = 'add-to-cart'),    
    path('cart/', views.showcart, name='cart'),

    path('mobile/', views.MobileView, name='mobile'),#for mobile filter all 
    path('mobile/<slug:data>/', views.MobileView, name='mobile-data'),# for mobile filter by data = brand
    
    path('laptop',views.laptopView , name = "laptop"),
    path('laptop/<slug:data>/',views.laptopView , name = "laptop-data"),

    path('bottomwear',views.Bottom_wear , name="bottomwear"),
    path('bottomwear/<slug:data>/',views.Bottom_wear, name = "bottomwear-data"),

    #customer activity urls
    path('buy/', views.buy_now, name='buy-now'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('address/', views.address, name='address'),
    path('orders/', views.orders, name='orders'),
    
    path('checkout/', views.checkout, name='checkout'),
] + static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT)
