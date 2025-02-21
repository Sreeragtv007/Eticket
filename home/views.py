from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response    
from .models import Events
from .serializers import Eventserializer
# Create your views here.


    
class event(APIView):
    
    def get(self,request):
        
        events = Events.objects.all()
        serializer = Eventserializer(events,many=True)
        
        return Response(serializer.data)