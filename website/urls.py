from django.urls import include, path
from .views import home, contact

urlpatterns = [
    path('', home,name='home'),
    path('contato', contact, name='contact'),
]