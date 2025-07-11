from django.urls import path
from .import views

urlpatterns = [

    path(r'panel/subcategory/list/', views.subcat_list, name='subcat_list'),   ## Admin Panel Subcategory List
    path(r'panel/subcategory/add/', views.subcat_add, name='subcat_add'),      ## Admin Panel Add Subcategory
    path(r'panel/subcategory/edit/<int:pk>/', views.subcat_edit, name='subcat_edit'),      ## Admin Panel Edit Subcategory
    path(r'panel/subcategory/del/<int:pk>/', views.subcat_del, name='subcat_del'),
]