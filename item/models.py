from django.db import models
from item.utils import get_item_data

# Create your models here.
class Item(models.Model):
    itemUrl=models.URLField(max_length=1000)
    itemName=models.CharField(max_length=100)
    itemPrice=models.BigIntegerField()
    itemImage=models.CharField(max_length=500)
    itemDescription=models.TextField()
    itemDate=models.DateTimeField(auto_now=True)
    itemNewPrice=models.BigIntegerField(blank=True, null=True)

    class meta:
        ordering=["itemDate"]
    
    def __str__(self):
        return self.itemName
    
    def save(self,*args,**kwargs):
        itemData=get_item_data(self.itemUrl)
        self.itemName=itemData['title']
        self.itemPrice=itemData['price']
        self.itemDescription=itemData['des']
        self.itemImage=itemData['imgurl']
        super().save(*args,**kwargs)
