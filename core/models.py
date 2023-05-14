from django.db import models

# Create your models here.

class Kaseta(models.Model):
    title = models.CharField(max_length=100)
    release_date = models.DateField()
    duration = models.IntegerField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    # image = models.ImageField(upload_to='images/', blank=True)
    availability = models.IntegerField()
    
    def __str__(self):
        return self.title


class Order(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=12)
    kasety = models.ManyToManyField(Kaseta)
    is_returned = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name