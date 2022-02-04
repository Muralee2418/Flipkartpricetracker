from django.urls import path
from . import views

urlpatterns=[path("",views.index,name="index"),
path("additem",views.addItem,name="additem"),
path("edit",views.refreshitem,name="refreshitem"),
path("delete",views.deleteitem,name="deleteitem"),
]
