from pyBunniApi.objects.transaction import Transaction
from pyBunniApi.resources.base import BaseListResource


class Transactions(BaseListResource[Transaction]):
    endpoint = 'transactions'
    model = Transaction
