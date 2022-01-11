#Django Packages/Librariese
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
#From within the app
from .models import Product
from .serializers import ProductSerializer

#Filtering and search options, visible in app
class ProductViewSet(viewsets.ModelViewSet):
  queryset = Product.objects.all()
  serializer_class = ProductSerializer
  filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
  filterset_fields = ['id', 'name', 'brand', 'price']
  search_fields = ['name', 'tags', 'brand', 'tags']
  ordering_fields = ['name', 'id', 'brand', 'price', 'quantity']
  
  