# shipments/urls.py
from django.urls import path
from .views import view_shipments, add_shipment, update_shipment, delete_shipment, sign_up, home, logout_view, home_for_unauthenticated, account_info, location_page


urlpatterns = [
    path('view/', view_shipments, name='view_shipments'),
    path('add/', add_shipment, name='add_shipment'),
    path('update/<int:shipment_id>/', update_shipment, name='update_shipment'),
    path('delete/<int:shipment_id>/', delete_shipment, name='delete_shipment'),
    path('sign_up/', sign_up, name='sign_up'),
    path('home/', home, name='home'),  # new URL pattern
    path('logout/', logout_view, name='logout_view'),  # new URL pattern
    path('', home_for_unauthenticated, name='home_for_unauthenticated'),  # new URL pattern for unauthenticated users
    path('account_info/', account_info, name='account_info'),  # new URL pattern
    path('location/', location_page, name='location_page'),  # Add this line

]
