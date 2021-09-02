from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('website.urls')),
    path('admin/', include('adminpanel.urls')),
    path('personal_account/', include('personalarea.urls')),
    path('admin_test/', admin.site.urls),
]
