from bll.contacts_bll import ContactBll
from fastapi import APIRouter
from domain.contact import Contact

router = APIRouter()
contact_bll = ContactBll("json")

@router.get("/contacts")
def get_contacts() -> list[Contact]:
    return contact_bll.retrieve_contacts().get("contacts",[])

@router.get("/contacts/search") 
def search_contacts(keyword:str)-> list[Contact]:
    return contact_bll.search_contacts(keyword).get("contacts",[])

@router.get("/contacts/search/{keyword}") 
def search_contacts(keyword:str)-> list[Contact]:
    return contact_bll.search_contacts(keyword).get("contacts",[])
