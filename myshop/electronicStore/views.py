# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render


from electronicStore.models import Laptop,Mobile,Tablet

from django.http import HttpResponse, HttpResponseRedirect

from django.conf import settings

# Create your views here.

def index(request):
    return render(request, 'index.html')
def aboutus(request):
    return render(request, 'aboutus.html')
def laptops(request):
    lst=Laptop.objects.all()
    return render(request,'laptops.html',{'x':lst})
def tablets(request):
    lst=Tablet.objects.all()
    return render(request,'tablets.html',{'x':lst})
def mobiles(request):
    lst=Mobile.objects.all()
    return render(request,'mobiles.html',{'x':lst})
lst=[]
price=[]
def kart_laptop(request,num):
    item=Laptop.objects.get(id=num)
    #item=get_list_or_404(FormalShirt,pk=num)
    lst.append(item)
    price.append(item.price)
    return render(request,'kart.html',{'x':lst,'tot_price':sum(price)})


def kart_tablet(request,num):
    item=Tablet.objects.get(id=num)
    #item=get_list_or_404(FormalShirt,pk=num)
    lst.append(item)
    price.append(item.price)
    return render(request,'kart.html',{'x':lst,'tot_price':sum(price)})


def kart_mobile(request,num):
    item=Mobile.objects.get(id=num)
    #item=get_list_or_404(FormalShirt,pk=num)
    lst.append(item)
    price.append(item.price)
    return render(request,'kart.html',{'x':lst,'tot_price':sum(price)})



