from django.urls import path
from .import views

urlpatterns = [

    path(r'panel/trending/', views.trending_add, name='trending_add'),   ## Admin Panel Trending Add
    path(r'panel/trending/del/<int:pk>/', views.trending_del, name='trending_del'),   ## Admin Panel Delete Trending
    path(r'panel/trending/edit/<int:pk>/', views.trending_edit, name='trending_edit'),   ## Admin Panel Edit Trending

]