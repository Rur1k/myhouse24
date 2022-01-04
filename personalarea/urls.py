from django.urls import path
from personalarea import views

urlpatterns = [
    path('', views.cabinet, name='cabinet'),
    path('flat_id=<int:id>', views.cabinet_summary, name='cabinet_summary'),
    path('oldmonth', views.cabinet_summary_oldmonth, name='cabinet_summary_oldmonth'),
    path('invoices', views.cabinet_invoices, name='cabinet_invoices'),
    path('invoices/flat_id=<int:flat_id>', views.cabinet_invoices, name='cabinet_invoices_to_flat'),
    path('invoice/<int:id>', views.cabinet_invoice_info, name='cabinet_invoice_info'),
    path('invoice/print/<int:id>', views.cabinet_invoice_print, name='cabinet_invoice_print'),
    path('invoice/pdf/<int:id>', views.cabinet_invoice_pdf, name='cabinet_invoice_pdf'),
    path('tariff/flat_id=<int:flat_id>', views.cabinet_tariff, name='cabinet_tariff'),
    path('message', views.cabinet_messages, name='cabinet_messages'),
    path('message/<int:id>', views.cabinet_message_info, name='cabinet_message_info'),
    path('master-request', views.cabinet_master_request, name='cabinet_master_request'),
    path('master-request/create', views.cabinet_master_request_create, name='cabinet_master_request_create'),
    path('master-request/delete=<int:id>', views.cabinet_master_request_delete, name='cabinet_master_request_delete'),
    path('profile', views.cabinet_profile, name='cabinet_profile'),
    path('profile/update', views.cabinet_profile_update, name='cabinet_profile_update'),

# Авторизация
    path('login', views.login_user, name='login_user'),
    path('logout', views.logout_user, name='logout_user'),

]