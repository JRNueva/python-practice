from util.file_util import read_json_as_dict
from dal.abstract_contacts import ContactsABC

class ContactsJsonDao(ContactsABC):
    def retrieve_contacts(self):
        return read_json_as_dict("contacts.json")