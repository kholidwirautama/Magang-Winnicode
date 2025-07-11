from django.urls import path
from .import views

urlpatterns = [

    path(r'blacklist/', views.black_list, name='black_list'), # Blacklist of IP
    path(r'blacklist/add/', views.ip_add, name='ip_add'),  # Add Blacklist of IP
    path(r'blacklist/del/<int:pk>/', views.ip_del, name='ip_del'), # Delete IP based on pk

]