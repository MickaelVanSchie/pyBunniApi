from pyBunniApi.objects.invoicedesign import InvoiceDesign
from pyBunniApi.resources.base import BaseListResource


class InvoiceDesigns(BaseListResource[InvoiceDesign]):
    endpoint = 'invoice-designs'
    model = InvoiceDesign
