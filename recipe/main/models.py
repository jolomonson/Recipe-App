from django.db import models

# Create your models here.
class Recipe(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=8)
    image = models.ImageField(upload_to='recipes/')
    date = models.DateTimeField(auto_now=True)
