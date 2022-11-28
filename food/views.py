from django.contrib.auth.models import User, Group
from django.http import HttpResponse

from rest_framework import permissions
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views    import APIView

from . models      import Food
from . serializers import FoodSerializer, UserSerializer, GroupSerializer


def index(request):
	return HttpResponse("<h1>Hello,{request.user} World</h1>")

class FoodList(APIView):
	
	def get(self, request, format=None):
		food1 = Food.objects.all()
		serializer = FoodSerializer(food1, many=True)
		return Response(serializer.data)

	def post(self, request, format=None):
		serializer = FoodSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserViewSet(viewsets.ModelViewSet):
	
	permission_classes = [permissions.AllowAny]
	queryset = User.objects.all().order_by('-date_joined')
	serializer_class = UserSerializer
	# authentication_classes = [permissions.IsAuthenticated]

	def get(self, format=None):
		users = User.objects.all()
		serializer = UserSerializer(users, many=True)
		return Response(serializer.data)

	def post(self, request):
		serializer = UserSerializer(data=request.data)
		if serializer.is_valid(raise_exception=ValueError):
			serializer.create(validated_data=request.data)
			return Response(
				serializer.data,
				status=status.HTTP_201_CREATED
			)
		return Response(
			{
				"error": True,
				"error_msg": serializer.error_messages,
			},
			status=status.HTTP_400_BAD_REQUEST
		)

	# 

class GroupViewSet(viewsets.ModelViewSet):

	queryset = Group.objects.all()
	serializer_class = GroupSerializer
	permission_classes = [permissions.IsAuthenticated]


class FoodDetail(APIView):

	def get_object(self, pk):
		try:
			return Food.objects.get(pk=pk)
		except Food.DoesNotExist:
			raise Http404

	def get(self, request, pk, format=None):
		Food = self.get_object(pk)
		serializer = FoodSerializer(Food)
		return Response(serializer.data)

	def put(self, request, pk, format=None):
		Food = self.get_object(pk)
		serializer = FoodSerializer(Food, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, pk, format=None):
		Food = self.get_object(pk)
		Food.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)

# Create your views here.
