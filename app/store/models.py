from django.db import models

class Customer(models.Model):
    first_name = models.CharField(max_length=90,null=False)
    last_name = models.CharField(max_length=90,null=False)
    address = models.CharField(max_length=500,null=False)
    city = models.CharField(max_length=50,null=False)
    email = models.EmailField(null=False)

    def __str__(self):
        return self.email


class Product(models.Model):
    name = models.CharField(max_length=200,null=False,unique=True)
    price = models.FloatField(null=False)

    def __str__(self):
        return self.name

class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    name = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

class Order(models.Model):
    order_date = models.DateField(null=False)
    shipped_date = models.DateField(null=False)
    delivered_date = models.DateField(null=False)
    coupon_code = models.CharField(max_length=50,null=True)
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE,null=False)
    products = models.ManyToManyField(Product,through='LineItem')

    def __str__(self):
        return self.customer.first_name

class LineItem(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE,null=False)
    product = models.ForeignKey(Product,on_delete=models.CASCADE,null=False)
    quantity = models.PositiveIntegerField(null=False)

    def __str__(self):
        return self.product.name