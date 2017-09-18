from .models import Duck
from rest_framework import serializer

class DuckSerializer(serializer.HyperLinkedModelSerializer):
	class Meta:
		model = Duck
		fields = ('id', 'name', 'lastnama', 'mail', 'age')