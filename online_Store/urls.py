"""
URL configuration for shopping_MS project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .import views



urlpatterns = [
    path('', views.home),
    path('product-detail/<id>', views.product_detail, name='product-detail'),
    path('add-to-cart/', views.add_to_cart, name='add-to-cart'),
    path('Cart', views.showcart, name='showcart'),
    path('pluscart/', views.pluscart, name='pluscart'),
    path('minuscart/',views.minuscart),
    path('removecart/',views.removecart),
    
    
    path('buy/', views.buy_now, name='buy-now'),
    path('profile/', views.profile, name='profile'),
    path('address/', views.address, name='address'),
    path('orders/', views.orders, name='orders'),
    path('changepassword/', views.change_password, name='changepassword'),
    path('mobile/', views.mobile, name='mobile'),
    path('mobile/<str:data>/',views.mobile, name='mobiledata'),
    path('laptops/', views.laptops, name='laptops'),
    path('laptops/<str:data>/',views.laptops ,name='laptopsdata'),
    path('topwear/',views.top,name='top'),
    path('topwear/<str:data>/',views.top,name='topdata'),
    path('bottomwear',views.bottom,name='bottomwear'),
    
    
    
    path('login/', views.login_page, name='login'),
    path('logout',views.logout_page,name='logout'),
    path('registration/', views.customerregistration, name='customerregistration'),
    path('checkout/', views.checkout, name='checkout'),
    path('checkout/paymentdone/',views.paymentdone, name='paymentdone'),
    path('search',views.search,name='search'),
]
