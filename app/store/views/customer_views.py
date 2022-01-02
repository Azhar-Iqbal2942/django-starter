from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny

# Custom Imports
from store.models import Customer
from store.serializers.customer_serializer import CustomerSerializer

class CustomerViewSet(ModelViewSet):
    permission_classes = (AllowAny,)
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer 
    
