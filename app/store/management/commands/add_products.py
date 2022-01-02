import faker_commerce
from faker import Faker
from django.core.management.base import BaseCommand

# Custom Imports
from store.models import Product 

class Command(BaseCommand):
    """Django command to create fake Products"""

    def handle(self, *args, **options):
        self.stdout.write("Operation Started to create fake products")
        fake =  Faker()
        fake.add_provider(faker_commerce.Provider)
        
        unique_product_name = {fake.ecommerce_name() for _ in range(1000)}
        unique_product_name = list(unique_product_name)
       
        if len((unique_product_name)) > 500:
            for i,_ in enumerate(range(500)):
                Product.objects.create(
                    name = unique_product_name[i],
                    price = float(fake.ecommerce_price())
                )
        else:
            self.stdout.write(self.style.ERROR("Products is less than 500, please try again!"))
            
        self.stdout.write(self.style.SUCCESS("Products created successfully"))