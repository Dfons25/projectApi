from flask_restplus import Api, Resource
from .api import endpoint as api_handler

"""
Module responsible for collecting all the namespaces into the same api
"""

api = Api(
    title='Mobile Computation - Project 1',
    version='1.0',
    description='API structure',
)

api.add_namespace(api_handler)

