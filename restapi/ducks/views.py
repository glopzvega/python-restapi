# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# from django.shortcuts import render

from rest_framework import generics
from .models import Duck
from .serializers import DuckSerializer
from django.shortcuts import get_object_or_404

# Create your views here.

class DuckList(generics.ListCreateAPIView):
	
	queryset = Duck.objects.all()
	serializer_class = DuckSerializer

	def get_object(self):
		queryset = self.queryset
		obj = get_object_or_404(
			queryset, 
			pk=self.kwargs['pk'],
		)
		return obj

