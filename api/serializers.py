#Django libraries
from rest_framework import serializers
#From app
from api.models import Product


#Serializers are used to render json and xml data
class ProductSerializer(serializers.ModelSerializer):
  class Meta:
    model = Product
    fields = '__all__'