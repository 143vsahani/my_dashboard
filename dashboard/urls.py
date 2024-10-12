
from django.urls import path
from django.contrib import admin
from .views import get_sales_data, dashboard_view  # Ensure imports are correct

urlpatterns = [
    path('api/sales/', get_sales_data, name='get_sales_data'),
    path('dashboard/', dashboard_view, name='dashboard_view'),
]
