from pyBunniApi.objects.bankaccount import BankAccount
from pyBunniApi.resources.base import BaseListResource


class BankAccounts(BaseListResource[BankAccount]):
    endpoint = 'bank-accounts'
    model = BankAccount
