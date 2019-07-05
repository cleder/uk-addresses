# -*- coding: utf-8 -*-
"""Address Admin"""

from django.contrib.gis import admin

from .models import Address

@admin.register(Address)
class AuthorAdmin(admin.OSMGeoAdmin):
    """Address admin."""

    list_display = ('postcode', 'source')
    list_filter = ('source', )
    search_fields = ['postcode']
