from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny

# Custom Imports
from store.models import Customer
from store.serializers.customer_serializer import CustomerSerializer

class CustomerList(APIView):
    permission_classes = (AllowAny,)
    
    def get(self,request):
        queryset = Customer.objects.all()
        serializer = CustomerSerializer(queryset,many=True)
        return Response(data=serializer.data)