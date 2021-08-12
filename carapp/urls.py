from django.contrib import admin
#from django.urls import path,include
from .views import show,orderdate_statewise,customerinfo,mail,city_det_ordernum,det_by_country,sales,func,complaint,employee,manage,payment
from carapp import views
from django.conf.urls import url, include

urlpatterns = [
   url(r'show/', show,name='create'),
   url(r'sales/', sales,name='create'),
   url(r'customerinfo/',customerinfo,name='create'),
   url(r'payment/',payment,name='create'),
   url(r'mail/', mail,name='create'),
   url(r'complaint/', complaint,name='create'),
   url(r'manage/', manage,name='create'),
   url(r'employee/', employee,name='create'),
   url(r'orderdate_statewise/', orderdate_statewise,name='create'),
   url(r'city_det_ordernum/', city_det_ordernum,name='create'),
   url(r'det_by_country/', det_by_country,name='create'),
   url(r'func/', func,name='create'),
   ]