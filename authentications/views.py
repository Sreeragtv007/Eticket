from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import CustomuserSerializer, UserSerializer
from django.contrib.auth.models import User
# Create your views here.


class userRegister(APIView):

    def post(self, request):
        serializer = CustomuserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response({"message": "User Registered Successfully"})
        else:
            return Response(serializer.errors)
