from django.urls import path
from .import views

urlpatterns = [

    path(r'', views.home, name='home'),                        ## Front Home Page
    path(r'about/', views.about, name='about'),                ## Front About Page
    path(r'panel/', views.panel, name='panel'),                ## Admin Panel Home Page
    path(r'login/', views.mylogin, name='mylogin'),            ## Front Login Page
    path(r'register/', views.myregister, name='myregister'),    ## Front Register Page
    path(r'logout/', views.mylogout, name='mylogout'),         ## Front Logoout Page
    path(r'panel/setting/', views.site_setting, name='site_setting'),  ## Admin Panel Settings
    path(r'panel/about/setting/', views.about_setting, name='about_setting'),  ## This is for about(about seeting) in admin panel
    path(r'contact/', views.contact, name='contact'),          ## Front Contact Pages
    path(r'panel/change/pass/', views.change_pass, name='change_pass'),  ## Password Change (By clicking setting button in admin pannel)

    path(r'category/<str:catname>/', views.category_detail, name='category_detail'),
    path(r'search/', views.search, name='search'),
]