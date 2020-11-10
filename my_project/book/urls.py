from django.urls import path,include
from book import views
from rest_framework import routers
from django.contrib import admin


router = routers.DefaultRouter()
router.register('list',views.ProductViewSet)
router.register('category',views.CategoryViewSet)

# path("auth/", include("djoser.urls")),


urlpatterns = [
    path('api/',include(router.urls)),
    path('hello/', views.HelloView.as_view(), name='hello'),
    path('api-token-auth/', views.CustomAuthToken.as_view())

]