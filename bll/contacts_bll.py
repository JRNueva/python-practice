from dal.contacts_dal import ContactsJsonDao
from dal.contacts_db_dal import ContactsDbDao

class ContactBll:
    def get_service_proxy_registry(self):
        return {
            "retrieve_contacts_json": ContactsJsonDao().retrieve_contacts,
            "retrieve_contacts_db": ContactsDbDao().retrieve_contacts
        }

    def retrieve_contacts(self, source):
        print(ContactsDbDao.get_db_connection)
        return self.get_service_proxy_registry().get(f"retrieve_contacts_{source}")()