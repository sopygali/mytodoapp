from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('task/<str:pk>/', views.task, name = 'task'),
    path('create-task/', views.createTask, name = 'create-task'),
    path('update-task/<str:pk>/', views.updateTask, name = 'update-task'),
    path('delete-task/<str:pk>/', views.deleteTask, name = 'delete-task'),
    path('login/', views.loginPage, name = 'login'),
    path('logout/', views.logoutPage, name = 'logout'),
    path('register/', views.registerPage, name = 'register'),



]