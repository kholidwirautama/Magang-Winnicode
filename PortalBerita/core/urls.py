from django.urls import include, path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
#from django.urls import path

urlpatterns = [
    path('api/', include('api.urls')),
    path(r'admin/' , admin.site.urls),      # Django Default Admin Panel
    path(r'', include('main.urls')),         # here main is an app name
    path(r'', include('news.urls')),         # here news is an app name
    path(r'', include('cat.urls')),          # here cat is an app name
    path(r'', include('subcat.urls')),       # here subcat is an app name
    path(r'', include('contactform.urls')),       # here contactform is an app name
    path(r'', include('trending.urls')),       # here trending is an app name
    path(r'', include('manager.urls')),       # here manager is an app name
    path(r'', include('newsletter.urls')),       # here newsletter is an app name
    path(r'', include('comment.urls')),       # here comment is an app name
    path(r'', include('blacklist.urls')),       # here blacklist is an app name (for IP)
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)