from util.file_util import read_json_as_dict

class ContactsJsonDao:
    def retrieve_contacts(self):
        return read_json_as_dict("contacts.json")