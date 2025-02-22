from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Events
from .serializers import Eventserializer
# Create your views here.


class event(APIView):

    def post(self, request):
        serializer = Eventserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    def patch(self, request, pk):
        event = Events.objects.get(id=pk)
        serializer = Eventserializer(event, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    def delete(self, request, pk):
        event = Events.objects.get(id=pk)
        event.delete()
        return Response('Event Deleted')
    
class showEvent(APIView):
    def get(self,request):
        
        events = Events.objects.all()
        serializer = Eventserializer(events,many=True)
        
        return Response(serializer.data)
