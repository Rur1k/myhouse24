from django.urls import path
from personalarea import views

urlpatterns = [
    path('', views.cabinet, name='cabinet'),
    path('flat_id=<int:id>', views.cabinet_summary, name='cabinet_summary'),
    path('oldmonth', views.cabinet_summary_oldmonth, name='cabinet_summary_oldmonth'),
    path('thisyear', views.cabinet_summary_thisyear, name='cabinet_summary_thisyear'),
    path('allyear', views.cabinet_summary_allyear, name='cabinet_summary_allyear'),
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
    path('profile?<int:user_id>', views.cabinet_profile, name='cabinet_profile_adm'),
    path('profile/update', views.cabinet_profile_update, name='cabinet_profile_update'),
    #Для админа
    path('user=<int:user_id>', views.cabinet, name='cabinet_adm'),
    path('user=<int:user_id>/flat_id=<int:id>', views.cabinet_summary, name='cabinet_summary_adm'),
    path('user=<int:user_id>/invoices', views.cabinet_invoices, name='cabinet_invoices_adm'),
    path('user=<int:user_id>/invoices/flat_id=<int:flat_id>', views.cabinet_invoices, name='cabinet_invoices_to_flat_adm'),
    path('user=<int:user_id>/invoice/<int:id>', views.cabinet_invoice_info, name='cabinet_invoice_info_adm'),
    path('user=<int:user_id>/invoice/print/<int:id>', views.cabinet_invoice_print, name='cabinet_invoice_print_adm'),
    path('user=<int:user_id>/invoice/pdf/<int:id>', views.cabinet_invoice_pdf, name='cabinet_invoice_pdf_adm'),
    path('user=<int:user_id>/tariff/flat_id=<int:flat_id>', views.cabinet_tariff, name='cabinet_tariff_adm'),
    path('user=<int:user_id>/message', views.cabinet_messages, name='cabinet_messages_adm'),
    path('user=<int:user_id>/message/<int:id>', views.cabinet_message_info, name='cabinet_message_info_adm'),
    path('user=<int:user_id>/master-request', views.cabinet_master_request, name='cabinet_master_request_adm'),
    path('user=<int:user_id>/master-request/create', views.cabinet_master_request_create, name='cabinet_master_request_create_adm'),
    path('user=<int:user_id>/master-request/delete=<int:id>', views.cabinet_master_request_delete, name='cabinet_master_request_delete_adm'),
    path('user=<int:user_id>/profile', views.cabinet_profile, name='cabinet_profile_adm'),
    path('user=<int:user_id>/profile/update', views.cabinet_profile_update, name='cabinet_profile_update_adm'),

# Авторизация
    path('login', views.login_user, name='login_user'),
    path('logout', views.logout_user, name='logout_user'),

]