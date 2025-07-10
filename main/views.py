from django.shortcuts import render, get_object_or_404
from .forms import CustomForms
from rest_framework.decorators import api_view
from rest_framework.response import Response
from main.models import Product, Order, OrderItem
from main.serializers import ProductSerializer, OrderItemSerializer, OrderSerializer

@api_view(['GET'])
def product_list(request):
    product = Product.objects.all()
    serializer = ProductSerializer(product, many=True)

    return Response(serializer.data)

@api_view(['GET'])
def product_details(request, pk):
    product = get_object_or_404(Product, pk=pk)
    serializer = ProductSerializer(product)
    return Response(serializer.data)

@api_view(['GET'])
def order_list(request):
    orders = Order.objects.all()
    serializer = OrderSerializer(orders, many=True)
    return Response(serializer.data)