# -*- coding: utf-8 -*-
"""FHRS Import"""
from django.core.management.base import BaseCommand
from addresses.importers import fhrs_import
from addresses.apis.fhrs import get_authorities_basic

class Command(BaseCommand):
    """Import establishment data from FHRS"""

    help = 'Imports establishment data from FHRS'

    def handle(self, *args, **options):
        """Import ALL FHRS establishments"""
        for auth in get_authorities_basic():
            print(auth['Name'])
            fhrs_import(auth['LocalAuthorityId'])
