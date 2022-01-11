from django.db import models
from uuid import uuid4
import datetime

def create_id():
    now = datetime.datetime.now()
    return str(now.year)+str(now.month)+str(uuid4())[:4]

#Product model
class Product (models.Model):
  name = models.CharField(max_length=255, unique=True)
  brand = models.CharField(max_length=255) 
  category = models.CharField(max_length=255) 
  tags = models.CharField(max_length=255)
  quantity = models.IntegerField()
  price = models.FloatField()
  date_added = models.DateTimeField(auto_now_add=True, editable=False)
  date_modified = models.DateTimeField(auto_now=True, editable=False)
  id = models.CharField(primary_key=True,max_length=200, default=create_id, editable=False)
   
  
  def __str__(self):
    return self.name
  

  
