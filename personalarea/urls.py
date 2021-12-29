from django.urls import path
from personalarea import views

urlpatterns = [
    path('', views.cabinet, name='cabinet'),
    path('flat_id=<int:id>', views.cabinet_summary, name='cabinet_summary'),
    path('invoices', views.cabinet_invoices, name='cabinet_invoices'),
    path('invoices/flat_id=<int:flat_id>', views.cabinet_invoices, name='cabinet_invoices_to_flat'),
    path('invoice/<int:id>', views.cabinet_invoice_info, name='cabinet_invoice_info'),
    path('tariff/flat_id=<int:flat_id>', views.cabinet_tariff, name='cabinet_tariff'),
    path('message', views.cabinet_messages, name='cabinet_messages'),
    path('message/<int:id>', views.cabinet_message_info, name='cabinet_message_info'),

# Авторизация
    path('login', views.login_user, name='login_user'),
    path('logout', views.logout_user, name='logout_user'),

]