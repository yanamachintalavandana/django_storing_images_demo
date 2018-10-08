# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Mobile(models.Model):
    name = models.CharField(max_length=30)
    photo = models.FileField(blank=True)
    description = models.TextField(max_length=500,blank=True)
    price=models.DecimalField(max_digits=10,decimal_places=2,null=True)
    available=models.BooleanField(default=True)
    stock=models.PositiveIntegerField(null=True)
    created=models.DateTimeField(auto_now_add=True,null=True)
    updated=models.DateTimeField(auto_now=True,null=True)
    def __str__(self):
        return '%s' %self.name

class Laptop(models.Model):
    name = models.CharField(max_length=30)
    photo = models.FileField(blank=True)
    description = models.TextField(max_length=500,blank=True)
    price=models.DecimalField(max_digits=10,decimal_places=2,null=True)
    available=models.BooleanField(default=True)
    stock=models.PositiveIntegerField(null=True)
    created=models.DateTimeField(auto_now_add=True,null=True)
    updated=models.DateTimeField(auto_now=True,null=True)
    def __str__(self):
        return '%s' %self.name

class Tablet(models.Model):
    name = models.CharField(max_length=30)
    photo = models.FileField(blank=True)
    description = models.TextField(max_length=500,blank=True)
    price=models.DecimalField(max_digits=10,decimal_places=2,null=True)
    available=models.BooleanField(default=True)
    stock=models.PositiveIntegerField(null=True)
    created=models.DateTimeField(auto_now_add=True,null=True)
    updated=models.DateTimeField(auto_now=True,null=True)
    def __str__(self):
        return '%s' %self.name
