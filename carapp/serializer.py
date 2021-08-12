# from .models import productLines
from .models import Carpro
# from student.serializers import studentSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import serializers
class carSerializer(serializers.ModelSerializer):
	class Meta:
		model = Carpro
		#model = productLines
		#fields = ['productLine','textDescription','htmlDescription']
		fields = ['productname','productline','ordernumber','quantityordered',
		'priceeach','orderdate','shippeddate','status','customernumber','customername','country']
                 
                 
        
        