from django.shortcuts import render

from rest_framework   import serializers
from . models         import foody

class foodySerializer(serializers.ModelSerializer):
	"""docstring for foodySerializer"""
	class Meta:
		model  = foody

		fields = '__all__'


# Create your views here.
