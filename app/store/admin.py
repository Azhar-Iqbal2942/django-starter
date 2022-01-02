from django.contrib import admin

# Custom Imports
from store.models import Customer,Order,LineItem,Product


# Register admin model here
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(LineItem)
admin.site.register(Product)
