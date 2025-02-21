from django.urls import path,include
from .views import userRegister
urlpatterns = [
    path('signup/',userRegister.as_view()),
]
