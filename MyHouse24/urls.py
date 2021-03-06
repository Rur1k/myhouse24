# import debug_toolbar
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('website.urls')),
    path('admin/', include('adminpanel.urls')),
    path('cabinet/', include('personalarea.urls')),
    path('admin_test/', admin.site.urls),
    # path('__debug__/', include(debug_toolbar.urls)),
]
