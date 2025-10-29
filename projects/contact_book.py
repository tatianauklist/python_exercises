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
        additionalContacts = input("Would you like to add anymore contact information? ")
        additionalContacts = additionalContacts.lower()
    if "yes" in additionalContacts:
        additionalMethods = input("Please input any additional contact information for the person: ")
        contactBook[contactName] = {"Preferred Method": contactMethod,contactMethod: contactInfo, "Additional Contacts": additionalMethods}
    

contactBook = {}

user_choice = menu()

addContacts()

user_wants_more = input("Would you like to add more contacts? ")
user_wants_more = user_wants_more.lower()

while user_wants_more == "yes":
    addContacts()
    user_wants_more = input("Would you like to add more contacts? ")
    user_wants_more = user_wants_more.lower()

print(contactBook)



