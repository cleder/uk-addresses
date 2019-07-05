# -*- coding: utf-8 -*-

import json
import requests

from pygeoif import geometry

base_url = 'http://api.ratings.food.gov.uk/'
headers = {
    'x-api-version': '2',
    'Accept': 'application/json',
}

FIELDS = {
    'external_id': 'FHRSID',
    'name:': 'BusinessName',
    'address_type': 'BusinessType',
    'address_line1': 'AddressLine1',
    'address_line2': 'AddressLine2',
    'address_line3': 'AddressLine3',
    'address_line4': 'AddressLine4',
    'postcode': 'PostCode',
    'phone': 'Phone',
}


def get_establishments(local_authority_id=None):
    """Get establisments for a local Authority Id."""
    params = {}
    if local_authority_id:
        params['localAuthorityId'] = local_authority_id
    url = base_url + 'Establishments'
    response = requests.get(url, params=params, headers=headers)
    response.raise_for_status()
    return response.json()['establishments']


def _to_geometry(geocode):
    """Convert the longitude and latitude into a point."""
    lat = geocode.get('latitude', 0)
    lon = geocode.get('longitude', 0)
    if lat or lon:
        return geometry.Point(float(lon), float(lat))


def parse_establishment(establishment):
    point = None
    if establishment.get('geocode', None):
        point = _to_geometry(establishment['geocode'])
    simplified = {'source': 'FHRS'}
    for f in FIELDS.keys():
        simplified[f] = establishment[FIELDS[f]]
    simplified['location'] = point
    return simplified



