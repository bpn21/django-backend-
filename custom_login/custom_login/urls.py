
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('custom_auth/', include('custom_auth.urls')),
]
