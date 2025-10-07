from dal.contacts_dal import ContactsJsonDao
from dal.contacts_db_dal import ContactsDbDao
from dal.abstract_contacts import ContactsABC

class ContactBll:
    def get_service_proxy_registry(self):
        return {
            "retrieve_contacts_json": ContactsJsonDao(),
            "retrieve_contacts_db": ContactsDbDao()
        }

    def retrieve_contacts(self, source):
        obj:ContactsABC = self.get_service_proxy_registry().get(f"retrieve_contacts_{source}")
        print(obj.__class__.mro())
        return obj.retrieve_contacts()
    
    