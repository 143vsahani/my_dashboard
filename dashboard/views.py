from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import ProductSales
from .serializers import ProductSalesSerializer
from django.shortcuts import render


@api_view(['GET'])
def get_sales_data(request):
    sales_data = ProductSales.objects.all()
    serializer = ProductSalesSerializer(sales_data, many=True)
    return Response(serializer.data)

def dashboard_view(request):
    return render(request, 'dashboard/dashboard.html')
