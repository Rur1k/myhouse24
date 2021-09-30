from django.urls import path
from website import views

urlpatterns = [
    path('', views.main, name='web_site_main'),
    path('about', views.about, name='web_site_about'),
    path('services', views.services, name='web_site_services'),
    path('contact', views.contact, name='web_site_contact'),
]