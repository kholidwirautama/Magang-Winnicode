from django.urls import path, re_path
from .import views

urlpatterns = [

    path(r'newsletter/add/', views.news_letter, name='news_letter'),
    path(r'panel/newsletter/emails/', views.news_emails, name='news_emails'),
    path(r'panel/newsletter/phones/', views.news_phones, name='news_phones'),
    path(r'panel/newsletter/del/<int:pk>/<int:num>/', views.news_txt_del, name='news_txt_del'),

]