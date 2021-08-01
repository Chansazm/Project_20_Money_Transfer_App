# -*- coding: utf-8 -*-

"""
    collection

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""

from collection.decorators import lazy_property
from collection.configuration import Configuration
from collection.controllers.api_controller import APIController


class CollectionClient(object):

    config = Configuration

    @lazy_property
    def client(self):
        return APIController()


    def __init__(self,
                 ocp_apim_subscription_key=None):
        if ocp_apim_subscription_key is not None:
            Configuration.ocp_apim_subscription_key = ocp_apim_subscription_key

