# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models



class TextMap(models.Model):
	doc_index = models.SmallIntegerField()
	words = models.CharField(max_length=300)
	frequency = models.SmallIntegerField()
