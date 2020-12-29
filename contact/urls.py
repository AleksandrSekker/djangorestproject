from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.CreateContact, name='add'),
    path('list/', views.contactList, name='list')
]
