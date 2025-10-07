from bll.contacts_bll import ContactBll
  
class Contacts:  
    
    def __init__(self, source="json"):
        self.contact_bll = ContactBll(source)
    
    def display_contacts(self):
        for record in self.contact_bll.retrieve_contacts().get("contacts"):
            print(f"Name: {record.get('name')}")
            print(f"Contact No: {record.get('contact_no')}")
            print()
            
    def search_contacts(self, keyword):
        for record in self.contact_bll.search_contacts(keyword).get("contacts"):
            print(f"Name: {record.get('name')}")
            print(f"Contact No: {record.get('contact_no')}")
            print()

            
# display_contacts()