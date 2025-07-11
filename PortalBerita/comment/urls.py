from django.urls import path
from .import views

urlpatterns = [

    path(r'comment/add/news/<int:pk>/', views.news_cm_add, name='news_cm_add'),
    path(r'comments/list/', views.comments_list, name='comments_list'), # Cooments list in Panel
    path(r'comments/del/<int:pk>/', views.comments_del, name='comments_del'), # Cooments delete in Panel
    path(r'comments/confirm/<int:pk>/', views.comments_confirm, name='comments_confirm'), # Cooments Confirm in Panel
]