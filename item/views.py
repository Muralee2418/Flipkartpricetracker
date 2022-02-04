from django.shortcuts import render, redirect
from item.models import Item
from item.forms import ItemForm
from item.utils import get_item_data

# Create your views here.
def addItem(request):
    items=Item.objects.all()
    if request.method=="POST":
        form=ItemForm(request.POST,request.FILES)
        if form.is_valid():
            newitem=form.save(commit=False)
            newitem.save()
            return render(request,"index.html",{"items":items})
    else:
        form=ItemForm()
    return render(request,"additem.html",{"form":form,'items':items})

def index(request):
    items=Item.objects.all()
    return render(request,"index.html",{"items":items})

def refreshitem(request):
      item_pk=request.POST.get("itempk")
      item=Item.objects.filter(pk=item_pk)
      itemobj=Item.objects.get(pk=item_pk)
      print(item)
      itemData=get_item_data(itemobj.itemUrl)
      item.update(itemNewPrice=itemData['price'])
      return redirect("index")
    
def deleteitem(request):
    item_pk=request.POST.get("itempk")
    item=Item.objects.filter(pk=item_pk)
    item.delete()
    return redirect("index")      