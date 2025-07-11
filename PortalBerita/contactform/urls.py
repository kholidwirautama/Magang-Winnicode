from django.urls import path
from .import views

urlpatterns = [

    path(r'contact/submit/', views.contact_add, name='contact_add'),  # when we click the send button, it will take me msgbox.html page
    path(r'panel/contactform/', views.contact_show, name='contact_show'),  # This is for admin panel
    path(r'panel/contactform/del/<int:pk>/', views.contact_del, name='contact_del'),  ## Messages Delete in admin panel
]