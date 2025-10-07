from bll.contacts_bll import ContactBll
  
class Contacts:  
    
    def __init__(self):
        self.contact_bll = ContactBll()
    
    def display_contacts(self, source="json"):
        for record in self.contact_bll.retrieve_contacts(source).get("contacts"):
            print(f"Name: {record.get('name')}")
            print(f"Contact No: {record.get('contact_no')}")
            print()
            
# display_contacts()