from django.urls import path
from . import views
urlpatterns = [
    # path('', views.index, name='index'),
    path('products/', views.product_list, name='products'),
    path('products/<int:pk>/', views.product_details, name="product_details"),
    path('orders/', views.order_list, name="order_list")
]