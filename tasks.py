# -*- coding: utf-8 -*-
"""Invoke file."""
import os
from invoke import task

PROJECT_DIR = os.path.dirname(__file__)
DB_NAME = 'uk_addresses'
DB_USER = 'django_addr'

@task
def createdb(ctx):
    pgpass = os.path.join(os.path.expanduser("~"), '.pgpass')

    with open(pgpass, 'r') as passfile:
        password = passfile.read().split(':')[-1]
    print(password)

    ctx.sudo('createuser {0} --superuser --createdb '.format(DB_USER), user='postgres')
    ctx.sudo('psql -c "ALTER USER {0} WITH PASSWORD \'{1}\'"'.format(DB_USER, password),
             user='postgres')
    ctx.sudo('createdb -O {0} {1}'.format(DB_USER, DB_NAME), user='postgres')
