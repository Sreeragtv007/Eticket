from django.urls import path,include
from .views import event
urlpatterns = [
    path('',event.as_view()),
]
