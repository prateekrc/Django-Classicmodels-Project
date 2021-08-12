from django.shortcuts import render
from django.db import connection
# Create your views here.
from itertools import chain
from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from .models import Carpro,products,productLines,orderDetails,Salesinfo,customers,orders,Complaint,Employees,Manage,Paymentinfo,Offices
from .serializer import carSerializer
from rest_framework.decorators import api_view
#from django.contrib.auth.models import User
#from django.contrib.auth import login,authenticate,logout
from django.conf import settings
from django.core.mail import send_mail

@api_view(['GET','POST'])
def show(request):
	if request.method == 'GET':
		queryset = productLines.objects.values('productLine','image','textDescription')
		return Response(queryset)
	if request.method == 'POST':
		data=request.data['productLine']
		queryset1=products.objects.values('productName','productCode','productLine','productDescription',
		'MSRP',).filter(productLine=data)	
		return Response(queryset1)

@api_view(['GET','POST'])
def sales(request):#total sales detail
	if request.method=='GET':
		queryset = Salesinfo.objects.values('customername','quantityordered','shippeddate','phone','state',
		'productcode','orderdate')
		return Response(queryset)

	if request.method == 'POST':#{productCode:S18_1589}
		productcode1 = request.data['productCode']
		queryset=products.objects.values('productName','productLine','productCode','productVendor',
		'MSRP').filter(productCode=productcode1)
		return Response(queryset)	

@api_view(['GET','POST'])
def customerinfo(request):
	if request.method== 'GET':
		emp=[]
		queryset=customers.objects.values('customerNumber','customerName','phone','city','country',
		'salesRepEmployeeNumber')
		emp.append(queryset)
		return Response(emp)

	if request.method == 'POST':
		var=request.data['customerName']#{"customerName":"Daedalus Designs Imports"}
		queryset=customers.objects.values('customerName','customerNumber','city','state','country',
		'phone').filter(customerName=var)
		return Response(queryset)
					

@api_view(['GET','POST','PUT'])
def payment(request):
	if request.method == 'GET':
		var = Paymentinfo.objects.values('customernumber','customername','amount','creditlimit','checknumber')
		return Response(var)

	if request.method == 'POST':
		var = request.data['checknumber'] #{"checknumber": "BO864823"}
		queryset = Paymentinfo.objects.values('customername','paymentdate','amount','phone','city','state','country',
		'salesrepemployeenumber').filter(checknumber=var)
		return Response(queryset)

	if request.method == 'PUT':
		var = request.data['customernumber']#{"customernumber":112}
		queryset = Paymentinfo.objects.values('customername','paymentdate','amount','city','state','country').filter(customernumber=var)
		return Response(queryset)

@api_view(['GET'])
def mail(request):
	if request.method == 'GET':
		#email = "shiwam.chaurasiya2000@gmail.com"
		subject ='Gentle Reminder'
		message ='Hi Dear customer your car needs to be serviced now Regards :) Carapp'
		email_from = settings.EMAIL_HOST_USER
		recipient_list =  ["shiwam.chaurasiya2000@gmail.com"]
		return Response(send_mail(subject,message,email_from,recipient_list))						

@api_view(['GET','POST'])
def complaint(request):
	if request.method == 'GET':
		queryset=orderDetails.objects.values('orderNumber')
		return Response(queryset)

	if request.method == 'POST':
		ordernumber1 = request.data['ordernumber']
		queryset = Complaint.objects.values('productline','productcode','productname','customername','ordernumber',
		'orderdate','quantityordered').filter(ordernumber=ordernumber1)
		return Response(queryset)		

@api_view(['GET','POST'])
def manage(request):#for employees
	if request.method == 'GET':
		var = Manage.objects.values('employeenumber','firstname','lastname','addressline1')
		return Response(var)

	if request.method == 'POST':#{"employeenumber":1702}
		var = request.data['employeenumber']
		queryset = Manage.objects.values('firstname','lastname','reportsto','jobtitle','postalcode').filter(employeenumber=var)
		return Response(queryset)	

@api_view(['GET','POST'])
def employee(request):
	if request.method == 'GET':
		queryset = Manage.objects.values('jobtitle','employeenumber','reportsto','addressline1')
		return Response(queryset)

	if request.method == 'POST':
		var = request.data['employeenumber']
		queryset = Employees.objects.values('jobtitle','firstname','lastname','jobtitle').filter(employeenumber=var)
		return Response(queryset)		

@api_view(['GET','POST'])
def orderdate_statewise(request):#sort by order date
	if request.method=='GET':
		this_list = Salesinfo.objects.values('customername','orderdate','productcode').order_by('orderdate')
		return Response(this_list)
	
	if request.method == 'POST':
		det=request.data['productCode'] # {"productCode":"S24_1937"}
		queryset = products.objects.values('productName','productLine','MSRP').filter(productCode=det)
		return Response(queryset)	


@api_view(['GET','POST'])
def city_det_ordernum(request):#all orders from Manchester
	if request.method == 'GET':
		queryset = Salesinfo.objects.values('customernumber','customername','ordernumber','productcode','quantityordered',
		'city').filter(city='Manchester')
		return Response(queryset)	

	if request.method == 'POST':
		city=request.data['ordernumber'] #{"ordernumber":10107}
		queryset = Complaint.objects.values('customername','productcode','productname','quantityordered','ordernumber',
		'orderdate').filter(ordernumber=city)
		return Response(queryset)	
			
@api_view(['GET','POST'])
def det_by_country(request):
	if request.method == 'GET':
		var = Offices.objects.values('officecode','phone','city','addressline1','postalcode','country')
		return Response(var)

	if request.method == 'POST':####
		det=request.data['country'] #country eg Australia
		queryset = Salesinfo.objects.values('customernumber','customername','ordernumber','city','state',
		'productcode','country').filter(country=det)
		return Response(queryset)


@api_view(['GET'])
def func(request):
	if request.method == 'GET':
		queryset = customers.objects.values('customerNumber', 'customerName').filter(customerNumber=112)
		queryset1 = orders.objects.values('orderDate','status')[:3]#.filter(customerNumber=103)
		dic={}
		dic1={}
		#dic2={}
		dic['k1']=queryset
		dic['k2']=queryset1
		#dic.update(dic1)
		#var=dic | dic1
		#dic3={**dic,**dic1}
		# for k in dic:
		# 	dic2['k']=dic['k1']
		# for k in dic1:
		# 	dic2['k2']=dic1['k2']	
		for i in dic:
			dict1={}
			dict1['X']=dic['k1'] 
			dict1['Y']=dic['k2']
		return Response(dic)			