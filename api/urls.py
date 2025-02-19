from django.urls import path,include

urlpatterns = [
    path('discover/',include('home.urls')),
]
