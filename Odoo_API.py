
def newContact(name,mobile,website):
    """ 
    Add a new Contact to the Odoo Data Base \n
    :return: returns the contact ID of the newly created contact
    """
    newContactID = models.execute_kw(db, uid, password, 'res.partner', 'create', [{'name': name, 'mobile':mobile,'website':website}])
    return newContactID

def listContacts(offset, limit):
    """
    List contacts starting from "offset" to a maximum of "limit" contacts\n
    return: returns nothing
    """
    contactID = models.execute_kw(db, uid, password,'res.partner', 'search', [[]],{'offset':offset,'limit':limit})
    contacts = models.execute_kw(db, uid, password, 'res.partner', 'read', [contactID],{'fields': ['id','name']})
    for contact in contacts:
        print(contact)

def getContactByID(contactID):
    contact = models.execute_kw(db, uid, password, 'res.partner', 'read', [contactID],{'fields': ['id','name']})
    return contact
    
def deleteContactById(contactID):
    models.execute_kw(db, uid, password, 'res.partner', 'unlink', [[contactID]])



## -----------------------------------------------------------------------------------
## Athentification
#Login Data
url = "https://zhaw.odoo.com"
db = "zhaw"
username = ''
password = ""

#Import xmlrpc module
import xmlrpc.client

#Call server
common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
version = common.version()

#Authenticate login
uid = common.authenticate(db, username, password, {})
models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))


## Authentification done
## -----------------------------------------------------------------------------------

listContacts(0,40)
ContactId = newContact("Philipp","079 100000", "email")
print(ContactId)
listContacts(0,40)







