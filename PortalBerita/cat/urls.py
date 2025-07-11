from django.urls import path
from .import views

urlpatterns = [

    path(r'panel/category/list/', views.cat_list, name='cat_list'),  ## For Admin Panel Category List
    path(r'panel/category/add/', views.cat_add, name='cat_add'),    ## For Admin Panel Category Add
    path(r'panel/category/edit/<int:pk>/', views.cat_edit, name='cat_edit'),
    path(r'export/cat/csv/', views.export_cat_csv, name='export_cat_csv'),    ## To download/export csv file
    path(r'import/cat/csv/', views.import_cat_csv, name='import_cat_csv'),    ## To import csv file

]






# word is a variable and d means digit. w means digit or number
# used P for received the value as a Parenthesis