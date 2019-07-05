# -*- coding: utf-8 -*-
"""Address Models"""

from django.contrib.gis.db import models

class Address(models.Model):

    source = models.CharField(blank=True, null=True, max_length=31)
    external_id = models.CharField(blank=True, null=True, max_length=255)
    name = models.CharField(blank=True, null=True, max_length=255)
    address_type = models.CharField(blank=True, null=True, max_length=255)
    address_line1 = models.CharField(blank=True, null=True, max_length=255)
    address_line2 = models.CharField(blank=True, null=True, max_length=255)
    address_line3 = models.CharField(blank=True, null=True, max_length=255)
    address_line4 = models.CharField(blank=True, null=True, max_length=255)
    address_line5 = models.CharField(blank=True, null=True, max_length=255)
    postcode = models.CharField(max_length=8, blank=True, null=True)
    phone = models.CharField(max_length=32, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    location = models.PointField(blank=True, null=True)
