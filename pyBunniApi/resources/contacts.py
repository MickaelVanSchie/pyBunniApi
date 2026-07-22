from pyBunniApi.objects.contact import Contact
from pyBunniApi.resources.base import BaseListResource


class Contacts(BaseListResource[Contact]):
    endpoint = 'contacts'
    model = Contact

    def get(self, contact_id: str) -> Contact:
        contact = self.bunni_api.create_http_request(f'contacts/get/{contact_id}')
        if self.bunni_api.TYPED:
            return Contact(**contact)
        return contact
