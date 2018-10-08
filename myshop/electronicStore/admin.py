# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from electronicStore.models import Laptop,Tablet,Mobile
# Register your models here.

admin.site.register(Laptop)
admin.site.register(Tablet)
admin.site.register(Mobile)

