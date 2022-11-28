from django.db import models

# from rest_framework.authtoken.models import token
# from django.db import forms


class Food(models.Model):
	
	name        = models.CharField('Name',max_length=10)	
	# food_id     = models.IntegerField('Id')	
	category_id = models.CharField('Category',max_length=10)
	discount    = models.FloatField('Discount')
	image_path  = models.FileField('Image')
	price       = models.FloatField('Price')

	def __str__(self):
		return self.name
# Create your models here.
