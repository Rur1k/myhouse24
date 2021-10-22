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
    # Управление сайтом
    path('website/home', views.website_home, name='website_home'),
    path('website/about', views.website_about, name='website_about'),
    path('website/about/deletephoto/<int:id>', views.website_about_delete_photo, name='about_delete_photo'),
    path('website/about/deletedopphoto/<int:id>', views.website_about_delete_dopphoto, name='about_delete_dopphoto'),
    path('website/services', views.website_services, name='website_services'),
    path('website/contact', views.website_contact, name='website_contact'),
    # Настройки системы
    path('setting/service', views.setting_service, name='setting_service'),
    path('setting/tariffs', views.setting_tariffs, name='setting_tariffs'),
    path('setting/tariffs/<int:id>', views.setting_tariffs_info, name='setting_tariffs_info'),
    path('setting/tariffs/create', views.setting_tariffs_create, name='setting_tariffs_create'),
    path('setting/tariffs/update/<int:id>', views.setting_tariffs_update, name='setting_tariffs_update'),
    path('setting/tariffs/delete/<int:id>', views.setting_tariffs_delete, name='setting_tariffs_delete'),
    path('setting/tariffs/create&copy=<int:id>', views.setting_tariffs_create, name='setting_tariffs_copy'),
    path('setting/tariffs/ajax/select_unit', views.select_service_unit, name='select_service_unit'),
    path('setting/user-admin/users', views.setting_user_admin, name='setting_user_admin'),
    path('setting/user-admin/<int:id>', views.setting_user_admin_info, name='setting_user_admin_info'),
    path('setting/user-admin/create', views.setting_user_admin_create, name='setting_user_create'),
    path('setting/user-admin/update/<int:id>', views.setting_user_admin_update, name='setting_user_update'),
    path('setting/user-admin/delete/<int:id>', views.setting_user_admin_delete, name='setting_user_delete'),
    path('setting/pay-company', views.setting_pay_company, name='setting_pay_company'),
    path('setting/transaction-purpose', views.setting_transaction_purpose, name='setting_transaction_purpose'),
    path('setting/transaction/create', views.setting_transaction_create, name='setting_transaction_create'),
    path('setting/transaction/update/<int:id>', views.setting_transaction_update, name='setting_transaction_update'),
    path('setting/transaction/delete/<int:id>', views.setting_transaction_delete, name='setting_transaction_delete'),
    # Владельцы квартир
    path('users', views.apartment_owner, name='apartment_owner'),
    path('user/create', views.apartment_owner_create, name='apartment_owner_create'),
    path('user/<int:id>', views.apartment_owner_info, name='apartment_owner_info'),
    path('user/update/<int:id>', views.apartment_owner_update, name='apartment_owner_update'),
    path('user/delete/<int:id>', views.apartment_owner_delete, name='apartment_owner_delete'),
    # Квартиры
    path('flat', views.flat, name='flat'),
    path('flat/create', views.flat_create, name='flat_create'),
    path('flat/info/<int:id>', views.flat_info, name='flat_info'),
    path('flat/update/<int:id>', views.flat_update, name='flat_update'),
    path('flat/delete/<int:id>', views.flat_delete, name='flat_delete'),
    path('flat/ajax/select_section_flat', views.select_section_flat, name='select_section_flat'),
    path('flat/ajax/select_floor_flat', views.select_floor_flat, name='select_floor_flat'),
    # Лицевые счета
    path('account', views.account, name='account'),
    path('account/create', views.account_create, name='account_create'),
    path('account/<int:id>', views.account_info, name='account_info'),
    path('account/update/<int:id>', views.account_update, name='account_update'),
    path('account/delete/<int:id>', views.account_delete, name='account_delete'),
    path('account/ajax/select_section_account', views.select_section_account, name='select_section_account'),
    path('account/ajax/select_flat_account', views.select_flat_account, name='select_flat_account'),
    path('account/ajax/order_flat_account', views.order_flat_account, name='order_flat_account'),
    path('account/ajax/select_username_account', views.select_username_account, name='select_username_account'),
    path('account/ajax/select_phone_account', views.select_phone_account, name='select_phone_account'),
    # Касса
    path('account-transaction', views.account_transaction, name='account_transaction'),

    # Авторизация
    path('login', views.login_admin, name='login_admin'),
    path('logout', views.logout_admin, name='logout_admin'),

]
