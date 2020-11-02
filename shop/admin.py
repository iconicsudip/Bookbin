from django.contrib import admin
from shop.models import Query
from shop.models import Contact
from shop.models import Product,Order#,OrdersUpdate

# Register your models here.
admin.site.register(Query)
admin.site.register(Contact)
admin.site.register(Product)
admin.site.register(Order)
#admin.site.register(OrdersUpdate)