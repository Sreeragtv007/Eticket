from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response    

# Create your views here.


class home_page(APIView):
    def get(self,request):
        return Response({'msg':'home page'})