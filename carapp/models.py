# Create your models here.
from django.db import models
#from django_mysql.models import JSONField, Model
class productLines(models.Model):
    productLine = models.CharField(max_length=50)
    htmlDescription = models.CharField(max_length=50)
    textDescription = models.CharField(max_length=100)
    image = models.ImageField()

    def __str__(self):
        return(self.productLine)

    class Meta:
        managed=False
        db_table='productlines'
class products(models.Model):
	productCode = models.CharField(max_length=50)
	productName = models.CharField(max_length=50)
	productLine = models.CharField(max_length=50)
	productScale = models.CharField(max_length=50)
	productVendor = models.CharField(max_length=50)
	productDescription = models.CharField(max_length=50)
	quantityInStock = models.IntegerField()
	buyPrice = models.IntegerField()
	MSRP = models.IntegerField()

	def __str__(self):
		return(self.productCode)

	class Meta:
		managed=False
		db_table = 'products'

class orderDetails(models.Model):
	orderNumber = models.IntegerField()
	productCode = models.IntegerField()
	quantityOrdered = models.IntegerField()
	priceEach = models.IntegerField()
	orderLineNumber = models.IntegerField()

	def __str__(self):
		return(self.orderNumber)

	class Meta:
		managed=False
		db_table = 'orderdetails'

class orders(models.Model):
	orderNumber = models.IntegerField()
	orderDate = models.DateField()
	requiredDate = models.DateField()
	shippedDate = models.DateField()
	status = models.CharField(max_length=100)
	comments = models.CharField(max_length=100)
	customerNumber = models.IntegerField()

	def __str__(self):
		return(self.orderNumber)

	class Meta:
		managed=False
		db_table='orders'




class customers(models.Model):
	customerName = models.CharField(max_length=100)
	customerNumber = models.IntegerField()
	customerLastName = models.CharField(max_length=100)
	customerFirstName = models.CharField(max_length=100)
	phone = models.IntegerField()
	addressLine1 = models.CharField(max_length=200)
	addressLine2 = models.CharField(max_length=200)
	city = models.CharField(max_length=100)
	state = models.CharField(max_length=100)
	postalCode = models.IntegerField()
	country = models.CharField(max_length=100)
	salesRepEmployeeNumber = models.IntegerField()
	creditLimit = models.IntegerField()

	class Meta:
		managed = False
		db_table = 'customers'
						

class Payments(models.Model):
    customernumber = models.OneToOneField(customers, models.DO_NOTHING, db_column='customerNumber', primary_key=True)  # Field name made lowercase.
    checknumber = models.CharField(db_column='checkNumber', max_length=50)  # Field name made lowercase.
    paymentdate = models.DateField(db_column='paymentDate')  # Field name made lowercase.
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'payments'
        unique_together = (('customernumber', 'checknumber'),)

class Employees(models.Model):
    employeenumber = models.IntegerField(db_column='employeeNumber', primary_key=True)  # Field name made lowercase.
    lastname = models.CharField(db_column='lastName', max_length=50)  # Field name made lowercase.
    firstname = models.CharField(db_column='firstName', max_length=50)  # Field name made lowercase.
    extension = models.CharField(max_length=10)
    email = models.CharField(max_length=100)
    officecode = models.ForeignKey('Offices', models.DO_NOTHING, db_column='officeCode')  # Field name made lowercase.
    reportsto = models.ForeignKey('self', models.DO_NOTHING, db_column='reportsTo', blank=True, null=True)  # Field name made lowercase.
    jobtitle = models.CharField(db_column='jobTitle', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'employees'

class Offices(models.Model):
    officecode = models.CharField(db_column='officeCode', primary_key=True, max_length=10)  # Field name made lowercase.
    city = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    addressline1 = models.CharField(db_column='addressLine1', max_length=50)  # Field name made lowercase.
    addressline2 = models.CharField(db_column='addressLine2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    state = models.CharField(max_length=50, blank=True, null=True)
    country = models.CharField(max_length=50)
    postalcode = models.CharField(db_column='postalCode', max_length=15)  # Field name made lowercase.
    territory = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'offices' 

class Manage(models.Model):
    employeenumber = models.IntegerField(db_column='employeeNumber')  # Field name made lowercase.
    firstname = models.CharField(db_column='firstName', max_length=50)  # Field name made lowercase.
    lastname = models.CharField(db_column='lastName', max_length=50)  # Field name made lowercase.
    officecode = models.CharField(db_column='officeCode', max_length=10)  # Field name made lowercase.
    reportsto = models.IntegerField(db_column='reportsTo', blank=True, null=True)  # Field name made lowercase.
    jobtitle = models.CharField(db_column='jobTitle', max_length=50)  # Field name made lowercase.
    city = models.CharField(max_length=50, blank=True, null=True)
    phone = models.CharField(max_length=50, blank=True, null=True)
    addressline1 = models.CharField(db_column='addressLine1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    state = models.CharField(max_length=50, blank=True, null=True)
    country = models.CharField(max_length=50, blank=True, null=True)
    postalcode = models.CharField(db_column='postalCode', max_length=15, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'manage'

class Paymentinfo(models.Model):
    customernumber = models.IntegerField(db_column='customerNumber')  # Field name made lowercase.
    customername = models.CharField(db_column='customerName', max_length=50)  # Field name made lowercase.
    phone = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50, blank=True, null=True)
    country = models.CharField(max_length=50)
    creditlimit = models.DecimalField(db_column='creditLimit', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    salesrepemployeenumber = models.IntegerField(db_column='salesRepEmployeeNumber', blank=True, null=True)  # Field name made lowercase.
    addressline1 = models.CharField(db_column='addressLine1', max_length=50)  # Field name made lowercase.
    checknumber = models.CharField(db_column='checkNumber', max_length=50, blank=True, null=True)  # Field name made lowercase.
    paymentdate = models.DateField(db_column='paymentDate', blank=True, null=True)  # Field name made lowercase.
    amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'paymentinfo'                       


class Carpro(models.Model):
    productcode = models.CharField(db_column='productCode', max_length=15)  # Field name made lowercase.
    productname = models.CharField(db_column='productName', max_length=70)  # Field name made lowercase.
    buyprice = models.DecimalField(db_column='buyPrice', max_digits=10, decimal_places=2)  # Field name made lowercase.
    productline = models.CharField(db_column='productLine', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ordernumber = models.IntegerField(db_column='orderNumber', blank=True, null=True)  # Field name made lowercase.
    quantityordered = models.IntegerField(db_column='quantityOrdered', blank=True, null=True)  # Field name made lowercase.
    priceeach = models.DecimalField(db_column='priceEach', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    orderlinenumber = models.SmallIntegerField(db_column='orderLineNumber', blank=True, null=True)  # Field name made lowercase.
    msrp = models.DecimalField(db_column='MSRP', max_digits=10, decimal_places=2)  # Field name made lowercase.
    orderdate = models.DateField(db_column='orderDate', blank=True, null=True)  # Field name made lowercase.
    requireddate = models.DateField(db_column='requiredDate', blank=True, null=True)  # Field name made lowercase.
    shippeddate = models.DateField(db_column='shippedDate', blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(max_length=15, blank=True, null=True)
    customernumber = models.IntegerField(db_column='customerNumber', blank=True, null=True)  # Field name made lowercase.
    customername = models.CharField(db_column='customerName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    contactfirstname = models.CharField(db_column='contactFirstName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    contactlastname = models.CharField(db_column='contactLastName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    phone = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    country = models.CharField(max_length=50, blank=True, null=True)
    creditlimit = models.DecimalField(db_column='creditLimit', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    paymentdate = models.DateField(db_column='paymentDate', blank=True, null=True)  # Field name made lowercase.
    amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    employeenumber = models.IntegerField(db_column='employeeNumber', blank=True, null=True)  # Field name made lowercase.
    lastname = models.CharField(db_column='lastName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(max_length=100, blank=True, null=True)
    jobtitle = models.CharField(db_column='jobTitle', max_length=50, blank=True, null=True)  # Field name made lowercase.
    state = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'carpro'

class Salesinfo(models.Model):
    ordernumber = models.IntegerField(db_column='orderNumber')  # Field name made lowercase.
    productcode = models.CharField(db_column='productCode', max_length=15)  # Field name made lowercase.
    quantityordered = models.IntegerField(db_column='quantityOrdered')  # Field name made lowercase.
    priceeach = models.DecimalField(db_column='priceEach', max_digits=10, decimal_places=2)  # Field name made lowercase.
    orderdate = models.DateField(db_column='orderDate', blank=True, null=True)  # Field name made lowercase.
    requireddate = models.DateField(db_column='requiredDate', blank=True, null=True)  # Field name made lowercase.
    shippeddate = models.DateField(db_column='shippedDate', blank=True, null=True)  # Field name made lowercase.
    customernumber = models.IntegerField(db_column='customerNumber', blank=True, null=True)  # Field name made lowercase.
    customername = models.CharField(db_column='customerName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    phone = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    state = models.CharField(max_length=50, blank=True, null=True)
    country = models.CharField(max_length=50, blank=True, null=True)
    salesrepemployeenumber = models.IntegerField(db_column='salesRepEmployeeNumber', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'salesinfo'


class Complaint(models.Model):
    productcode = models.CharField(db_column='productCode', max_length=15)  # Field name made lowercase.
    productname = models.CharField(db_column='productName', max_length=70)  # Field name made lowercase.
    productline = models.CharField(db_column='productLine', max_length=50)  # Field name made lowercase.
    ordernumber = models.IntegerField(db_column='orderNumber', blank=True, null=True)  # Field name made lowercase.
    quantityordered = models.IntegerField(db_column='quantityOrdered', blank=True, null=True)  # Field name made lowercase.
    priceeach = models.DecimalField(db_column='priceEach', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    orderdate = models.DateField(db_column='orderDate', blank=True, null=True)  # Field name made lowercase.
    customername = models.CharField(db_column='customerName', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'complaint'                    
			