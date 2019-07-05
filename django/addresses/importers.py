# -*- coding: utf-8 -*-
"""Address Models"""
import logging

from .models import Address
from .apis.fhrs import get_establishments
from .apis.fhrs import parse_establishment

logger = logging.getLogger(__name__)


def fhrs_import(local_authority_id):
    establisments = get_establishments(local_authority_id)
    for est in establisments:
        ed = parse_establishment(est)
        logger.info('Create FHRS establishment %s', ed)
        Address.objects.create(**ed)
