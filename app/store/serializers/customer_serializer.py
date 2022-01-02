from rest_framework import serializers

# Custom Imports
from store.models import Customer 

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id','first_name','last_name','address','city','email']
        read_only_fields = ('id', )


