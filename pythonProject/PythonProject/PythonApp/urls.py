from django.urls import path
from .views import *

urlpatterns = [
    path('RegistrationApi/',RegistrationApi.as_view())
]