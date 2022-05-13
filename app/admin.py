from itertools import product
from django.contrib import admin
from .models import Product , Cart , Customer , OrderPlaced
# Register your models here.


# admin.site.register(product),
# admin.site.register(Customer),
# admin.site.register(Cart),
# admin.site.register(OrderPlaced),

@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','name','locality','city','zipcode','state']

@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = [
        'id' , 'title','selling_price','discounted_price','description','brand','category','product_img'
    ]

@admin.register(Cart)
class CartModelAdmin(admin.ModelAdmin):
    list_display = [
        'id','user','product' , 'quantity'
    ]

@admin.register(OrderPlaced)
class OrderPlacedModelAdmin(admin.ModelAdmin):
    list_display = [
        'id','user','customer','product','quantity','status'
    ]
