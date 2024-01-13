from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),  # for login/logout views
    path('shipment/', include('shipment.urls')),
    path('', include('shipment.urls')),
]
