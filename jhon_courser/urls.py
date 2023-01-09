from django.urls import include, path

from django.contrib import admin

urlpatterns = [
    path('', include('website.urls')),
    path('admin/', admin.site.urls),
]
