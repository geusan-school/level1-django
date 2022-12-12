from django.shortcuts import render
from rest_framework import viewsets
from products.models import Product
from products.serializers import ProductSerializer
from rest_framework.permissions import IsAdminUser
from products.permissions import IsReadOnly, IsAdminUserOrReadOnly

# Create your views here.
class ProductModelViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsAdminUserOrReadOnly,)
