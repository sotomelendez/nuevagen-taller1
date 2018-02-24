from django.db import models

# Create your models here.
class Category(models.Model):
	name = models.CharField(max_length=200)
	product_type = models.CharField(max_length=200)

class Provider(models.Model):
	name = models.CharField(max_length=200)
	address = models.CharField(max_length=200)
	contact_name = models.CharField(max_length=200)
	contact_phone = models.CharField(max_length=200)
	category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)