from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview, name='api-overview'),
    path('task-list/', views.taskList, name='task-list'),
    path('task-create/', views.TaskCreate, name='task-creaet'),
    path('task-update/<str:pk>/', views.TaskUpdate, name='task-update'),
    path('task-delete/<str:pk>/', views.TaskDelete, name='task-delete'),

]
