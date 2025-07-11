from django.urls import path
from .import views

urlpatterns = [

    path(r'news/<str:word>/', views.news_detail, name='news_detail'),       ## Front News Details Page
    path(r'panel/news/list/', views.news_list, name='news_list'),           ## Admin Panel News List
    path(r'panel/news/add/', views.news_add, name='news_add'),              ## Admin Panel Add News
    path(r'panel/news/del/<int:pk>/', views.news_delete, name='news_delete'),   ## Admin Panel Delete News
    path(r'panel/news/edit/<int:pk>/', views.news_edit, name='news_edit'),      ## Admin Panel Edit News
    path(r'panel/news/publish/<int:pk>/', views.news_publish, name='news_publish'), ## Admin Panel Publish News
    path(r'urls/<int:pk>/', views.news_detail_short, name='news_detail_short'),   ## Front News Short Url

]






# # word is a variable and d means digit. w means digit or number
# # used P for received the value as a Parenthesis