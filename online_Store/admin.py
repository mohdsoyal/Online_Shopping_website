from django.contrib import admin
from .models import Custumer,Product,Cart,Orderplaced
# Register your models here.

class custumerAdmin(admin.ModelAdmin):
    list_display =['user','name','locality','city','zipcode','state']
admin.site.register(Custumer,custumerAdmin)

class productAdmin(admin.ModelAdmin):
    list_display =['title','selling_price','discount_price','discription','brand','category','img'] 
admin.site.register(Product,productAdmin)


class cartAdmin(admin.ModelAdmin):
    list_display =['user','product','quantity']
admin.site.register(Cart,cartAdmin)


class orderplacedAdmin(admin.ModelAdmin):
    list_display =['user','customer','product','quantity','order_date','status']   
admin.site.register(Orderplaced,orderplacedAdmin)     
        