from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from . import views

from core import settings
from django.conf.urls.static import static

from .views import (
    UserViewSet,
    CategoryViewSet,
    SubcategoryViewSet,
    NewsletterViewSet,
    NewsViewSet,
    ContactFormViewSet,
    CommentViewSet,
)

router = DefaultRouter()
router.register(r"users", UserViewSet)
router.register(r"categories", CategoryViewSet)
router.register(r"subcategories", SubcategoryViewSet)
router.register(r"newsletters", NewsletterViewSet)
router.register(r"news", NewsViewSet)
router.register(r"contactforms", ContactFormViewSet)
router.register(r"comments", CommentViewSet)


urlpatterns = [
    path("", include(router.urls)),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),

    # HOME
    path('lastnews2/', views.LastNews2View.as_view()),
    path('popularnews/', views.PopularNewsView.as_view()),

    # NEWS DETAIL
    path('users/me/', views.CurrentUserView.as_view(), name='current_user'),

    # LOG IN
]
