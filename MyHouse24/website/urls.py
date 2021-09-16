from django.urls import path
from website import views

urlpatterns = [
    path('', views.main, name='web_site_main'),
]