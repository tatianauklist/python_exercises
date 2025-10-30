import json

def loadData():
    with open("contact_book.json","r") as fp:
        contactBook = json.load(fp)
        return(contactBook)
def menu():
    menuOptions = input("What would you like to do today? ")
    options = menuOptions.lower()
    return(options)
    
def addContacts():
    if "add" in user_choice:
        contactName = input("What is your contact's name? ")
        contactMethod = input("What is the contact method you're entering? ")
        contactInfo = input("What is the contact number or email you would like to save? ")
        contactBook[contactName] = {"Preferred Method": contactMethod, contactMethod: contactInfo} 
        additionalContacts = input("Would you like to add any more contact information? ")
        additionalContacts = additionalContacts.lower()
    if "yes" in additionalContacts:
        additionalMethods = input("Please input any additional contact information for the person: ")
        contactBook[contactName] = {"Preferred Method": contactMethod,contactMethod: contactInfo, "Additional Contacts": additionalMethods}
    

contactBook = {}
contactBook = loadData()

user_choice = menu()

addContacts()

user_wants_more = input("Would you like to add more contacts? ")
user_wants_more = user_wants_more.lower()

while user_wants_more == "yes":
    addContacts()
    user_wants_more = input("Would you like to add more contacts to your book? ")
    user_wants_more = user_wants_more.lower()

with open("contact_book.json","w") as fp:
    json.dump(contactBook,fp)
    




