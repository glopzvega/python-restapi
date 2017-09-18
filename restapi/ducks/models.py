# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Duck(models.Model):
	name = models.CharField(max_length=255)
	lastname = models.CharField(max_length=255)
	mail = models.EmailField(max_length=255)
	age = models.IntegerField()
