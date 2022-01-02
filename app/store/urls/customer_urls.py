from django.urls import path

# Custom Imports
from store.views.customer_views import CustomerList

urlpatterns = [
    path('',CustomerList.as_view())
   
]
