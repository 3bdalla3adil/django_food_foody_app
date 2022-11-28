from django.shortcuts        import render

from django.http             import HttpResponse
from django.shortcuts        import get_object_or_404

from rest_framework.views    import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework          import status
from rest_framework          import viewsets
from rest_framework          import permissions

from . models                import foody
from . serializers           import foodySerializer


class foodylist(APIView):
	
	def get(self,request):
		foody1     = foody.objects.all()
		serializer = foodySerializer(foody1,many=True)
		return Response (serializer.data)

	def post(self,request):
		serializer = foodySerializer(data=request.data,many=True)
		if serializer.is_valid():
			return Response (serializer.data)

# Create your views here.
