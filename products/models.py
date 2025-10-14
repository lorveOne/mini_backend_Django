from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def __str__(self):
        return self.name



class Order(models.Model):
   customer_email = models.EmailField()
   status = models.CharField(max_length=20, 
   choices=[('created', 'Created'), ('paid', 'paid'), ('canceled', 'Canceled')])
   created_at = models.DateTimeField(auto_now_add=True)
   total_price = models.DecimalField(max_digits=10, decimal_places=2)
   