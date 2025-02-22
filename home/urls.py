from django.urls import path,include
from .views import event,showEvent
urlpatterns = [
    path('',event.as_view()),
    path('show-events/',showEvent.as_view()),
]
