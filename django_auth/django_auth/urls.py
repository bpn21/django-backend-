from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('default_auth/',include('default_auth.urls')), 
]
