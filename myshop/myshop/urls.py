"""mystore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from electronicStore.views import index,aboutus,kart_laptop,kart_mobile,kart_tablet,laptops,mobiles,tablets
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',index),
    url(r'aboutus/$',aboutus),
    url(r'^laptops/$',laptops),
    url(r'^mobiles/$',mobiles),
    url(r'^tablets/$',tablets),
    url(r'^laptops/Kart(\d{1,3})/$',kart_laptop),
    url(r'^mobiles/Kart(\d{1,3})/$',kart_mobile),
    url(r'^tablets/Kart(\d{1,3})/$',kart_tablet)
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


admin.site.site_header =' My electronics shop website'
admin.site.index_title='Site features area'
