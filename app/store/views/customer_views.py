from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny

# Custom Imports
from store.models import Customer
from store.serializers.customer_serializer import CustomerSerializer

class CustomerList(ListCreateAPIView):
    permission_classes = (AllowAny,)
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer 

class CustomerDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (AllowAny,)
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer 
