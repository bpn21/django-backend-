from django.urls import path,include
from book import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('list',views.ProductViewSet)
router.register('category',views.CategoryViewSet)


urlpatterns = [
    path('api/',include(router.urls))
]