from django.shortcuts import render
from django.contrib.auth.models import User, Group

from rest_framework.validators import UniqueTogetherValidator
from rest_framework import serializers

from . models       import Food

class FoodSerializer(serializers.ModelSerializer):

	class Meta:
		model  = Food

		fields = '__all__'

class UserSerializer(serializers.HyperlinkedModelSerializer):
	def create(self,validated_data):
		user = User.objects.create_user(**validated_data)
		return user

	class Meta:
		model  = User
		fields = (
			'username',
			'email'   ,
			'password',
		)
		validators = [
			UniqueTogetherValidator(
				queryset=User.objects.all(),
				fields= ['username','email']
			)
		]

class GroupSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model  = Group
		fields = '__all__'

# Create your views here.
