from rest_framework import serializers

# Custom Imports
from store.models import Product 

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id','name','price']
        read_only_fields = ('id', )


