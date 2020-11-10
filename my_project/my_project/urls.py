from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url
from book import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('book.urls')),
    path("auth/", include("djoser.urls.jwt")),


    # path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
]