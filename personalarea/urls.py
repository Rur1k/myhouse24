from django.urls import path
from personalarea import views

urlpatterns = [
    path('', views.cabinet, name='cabinet'),
    path('flat_id=<int:id>', views.cabinet_summary, name='cabinet_summary'),
    path('invoices', views.cabinet_invoices, name='cabinet_invoices'),

# Авторизация
    path('login', views.login_user, name='login_user'),
    path('logout', views.logout_user, name='logout_user'),

]