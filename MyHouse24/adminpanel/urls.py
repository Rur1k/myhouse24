from django.urls import path
from adminpanel import views

urlpatterns = [
    path('', views.admin, name='admin'),
    # Дома
    path('house/', views.house, name='house'),
    path('house/create', views.create_house, name='create_house'),
    path('house/<int:id>', views.info_house, name='info_house'),
    path('house/update/<int:id>', views.update_house, name='update_house'),
    # Авторизация
    path('login/', views.login_admin, name='login_admin'),
    path('logout/', views.logout_admin, name='logout_admin'),

]
