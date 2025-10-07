import sqlite3

class ContactsDbDao:
    
    def get_db_connection(self):
        return sqlite3.connect('address_book.db')

    def retrieve_contacts(self):
        sql = "SELECT name, contact_no FROM contacts"
        
        conn = self.get_db_connection()
        cursor = conn.execute(sql)
        
        result = {
            "contacts": []
        }
        
        for row in cursor:
            result["contacts"].append({
                "name": row[0],
                "contact_no": row[1]
            })

        return result
