""" Script used to call the transactions service"""

from vesicashapi.base import VesicashBase

class Transactions(VesicashBase):
    @classmethod
    def create(cls, **kwargs):
        return cls().requests.post('transactions/create', data=kwargs)

