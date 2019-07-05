# -*- coding: utf-8 -*-
"""Address Admin"""

from django.contrib.gis import admin

from .models import Address

admin.site.register(Address, admin.OSMGeoAdmin)
