from django.urls import path
from . import views

urlpatterns = [
    # Define your URL patterns for the 'contact' app here
    # Example:
    path('', views.contact, name='contact'),
]
