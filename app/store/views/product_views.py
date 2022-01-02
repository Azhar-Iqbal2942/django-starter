from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny

# Custom Imports
from store.models import Product
from store.serializers.product_serializer import ProductSerializer



class ProductViewSet(ModelViewSet):
    permission_classes = (AllowAny,)
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

