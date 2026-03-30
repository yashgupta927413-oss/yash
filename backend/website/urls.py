from django.urls import path
from .views import homepage_data

urlpatterns = [
    path('homepage/', homepage_data, name='homepage-data'),
]
