from django.contrib.auth.models import User, Group
from rest_framework import serializers
from taller1.microservicio1.models import *


class UserSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = User
		fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Group
		fields = ('url', 'name')

class CategorySerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Category
		fields = ('url', 'name','product_type')

class ProvviderSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Provider
		fields = ('url', 'name', 'address', 'contact_name', 'contact_phone', 'category')

