from bll.contacts_bll import ContactBll
from fastapi import FastAPI
from domain.contact import Contact

app = FastAPI()
contact_bll = ContactBll("json")

@app.get("/contacts")
def get_contacts() -> list[Contact]:
    return contact_bll.retrieve_contacts().get("contacts",[])

@app.get("/contacts/search") 
def search_contacts(keyword:str)-> list[Contact]:
    return contact_bll.search_contacts(keyword).get("contacts",[])

@app.get("/contacts/search/{keyword}") 
def search_contacts(keyword:str)-> list[Contact]:
    return contact_bll.search_contacts(keyword).get("contacts",[])
