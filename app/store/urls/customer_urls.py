from django.urls import path

# Custom Imports
from store.views.customer_views import CustomerList,CustomerDetail

urlpatterns = [
    path('',CustomerList.as_view()),
    path('<int:pk>',CustomerDetail.as_view())
   
]
