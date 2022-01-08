#Django Packages/Librariese
from rest_framework import viewsets
#From within the app
from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
  queryset = Product.objects.all()
  serializer_class = ProductSerializer
  
class CategoryViewSet(viewsets.ModelViewSet):
  queryset = Category.objects.all()
  serializer_class = CategorySerializer