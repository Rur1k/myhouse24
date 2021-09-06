from django.urls import path
from adminpanel import views

urlpatterns = [
    path('', views.admin, name='admin'),
    path('house/', views.house, name='house'),
    path('login/', views.login, name='login'),

]
