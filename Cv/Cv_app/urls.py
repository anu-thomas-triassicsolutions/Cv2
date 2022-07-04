from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name='home'),
    path('display/<int:cv_id>/', views.display, name='display'),
    path('add/', views.add, name='add'),
    path('update/<int:id>/', views.update, name='update'),
]
