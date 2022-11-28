from django.db import models


class foody(models.Model):
	name        = models.CharField('Name',max_length=10)	
	food_id     = models.IntegerField('Id')
	category_id = models.CharField('Category',max_length=10)
	taken       = models.BooleanField('Taken',default=False)
	# image_path  = models.ImageField ('Image')
	price       = models.FloatField('Price',default=50)

	def __str__(self):
		return self.name

# Create your models here.
