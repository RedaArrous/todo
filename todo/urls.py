from django.urls import path, include
from . import views

app_name = 'todo'

urlpatterns = [
    path('', views.home_view, name='home'),
    path('add/', views.add_view, name="add"),
    path('edit/<int:pk>/', views.edit_view, name='edit'),
    path('delete/<int:pk>/', views.delete_view, name='delete'),

]
