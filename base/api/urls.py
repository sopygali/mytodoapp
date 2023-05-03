from django.urls import path, include
from . import views

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,)

from base.api.views import UserViews
from rest_framework.routers import DefaultRouter


urlpatterns = [
    path('', views.getRoutes),
    path('tasks/', views.getTasks),
    path('tasks/<str:pk>/', views.getTask),
    path('create-task/', views.createTask),
    path('update-task/<str:pk>', views.updateTask),
    path('delete-task/<str:pk>', views.deleteTask),
    path('api-auth/', include('rest_framework.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('marks/', views.getMarks),
    path('mark/<str:pk>', views.getMark),
    path('create-mark/', views.createMark),
    path('update-mark/<str:pk>/', views.updateMark),
    path('delete-mark/<str:pk>/', views.deleteMark),

]

router = DefaultRouter()
router.register('user', UserViews, basename='user')

urlpatterns += router.urls