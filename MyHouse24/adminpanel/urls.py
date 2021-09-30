from django.urls import path
from adminpanel import views

urlpatterns = [
    path('', views.admin, name='admin'),
    # Дома
    path('house', views.house, name='house'),
    path('house/create', views.create_house, name='create_house'),
    path('house/<int:id>', views.info_house, name='info_house'),
    path('house/update/<int:id>', views.update_house, name='update_house'),
    path('house/delete/<int:id>', views.delete_house, name='delete_house'),
    #Управление сайтом
    path('website/home', views.website_home, name='website_home'),
    path('website/about', views.website_about, name='website_about'),
    path('website/about/deletephoto/<int:id>', views.website_about_delete_photo, name='about_delete_photo'),
    path('website/about/deletedopphoto/<int:id>', views.website_about_delete_dopphoto, name='about_delete_dopphoto'),
    path('website/services', views.website_services, name='website_services'),
    path('website/contact', views.website_contact, name='website_contact'),

    # Авторизация
    path('login', views.login_admin, name='login_admin'),
    path('logout', views.logout_admin, name='logout_admin'),

]
