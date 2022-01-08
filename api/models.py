from django.db import models

class Category(models.Model):
  name = models.CharField(max_length=255, unique=True)
  tags = models.TextField(max_length=255)
  
  def __str__(self):
        return self.name
  
  def get_products(self):
    return Product.objects.filter(category=self.name)

class Product (models.Model):
  category = models.ForeignKey(Category, on_delete=models.CASCADE)
  name = models.CharField(max_length=255, unique=True)
  brand = models.CharField(max_length=255)  
  description = models.TextField(max_length=255)
  quantity = models.IntegerField()
  price = models.IntegerField()
  date_added = models.DateTimeField(auto_now_add=True, editable=False)
  date_modified = models.DateTimeField(auto_now=True, editable=False)
  id = models.PositiveIntegerField(primary_key=True, unique=True)
   
  
  def __str__(self):
    return self.name
  

  
