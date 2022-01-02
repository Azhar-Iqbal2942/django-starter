from faker import Faker
from django.core.management.base import BaseCommand

# Custom Imports
from store.models import Customer 

class Command(BaseCommand):
    """Django command to create fake customers"""

    def handle(self, *args, **options):
        self.stdout.write("Operation Started to create fake customers")
        fake = Faker()
        for _ in range(100):
            full_name = str(fake.name()).split(' ') 
            Customer.objects.create(
                first_name = full_name[0],
                last_name = full_name[1],
                address = fake.address(),
                city = fake.city(),
                email = fake.email()
            )
        self.stdout.write(self.style.SUCCESS("Customers created successfully"))