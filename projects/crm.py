import sqlite3


def loadData():
    sqlite3Connection = sqlite3.Connection("crm_database.db")
    cursor = sqlite3Connection.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS organizations(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            industry TEXT NOT NULL,
            website TEXT,
            notes TEXT
                   )
    ''' )
    cursor.execute(''' 
        CREATE TABLE IF NOT EXISTS contacts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE,
            phone TEXT,
            organizationID INTEGER,
            isPrimary INTEGER DEFAULT 0,
            FOREIGN KEY (organizationID) REFERENCES organizations(Id)          
            )               
    ''')
    sqlite3Connection.commit()
    sqlite3Connection.close()
    return("Database Initiated")
    
def addOrganization():
    sqlite3Connection = sqlite3.Connection("crm_database.db")
    cursor = sqlite3Connection.cursor()
    orgName = input("Organization Name: ")
    orgIndustry = input("Organization Industry: ")
    websiteOption = input("Is there an organization website? ").lower()
    orgWebsite = None
    if websiteOption == "yes":
        orgWebsite = input("Organization Website: ")
    orgNotes = None
    notesChoice = input("Would you like to any notes? ").lower()
    if notesChoice == "yes":
        orgNotes = input("Notes: ")
    sql_statement = '''INSERT INTO organizations(name, industry, website, notes) VALUES (?,?,?,?)'''
    cursor.execute(sql_statement,(orgName,orgIndustry,orgWebsite,orgNotes))
    newOrgID = cursor.lastrowid
    sqlite3Connection.commit()
    print("Organization added successfully\nClosing connection...")
    sqlite3Connection.close()
    return(f"{orgName}: {newOrgID}")
    
def addContacts():
    conn = sqlite3.Connection("crm_database.db")
    cursor = conn.cursor()
    contactName = input("Contact Name: ")
    contactEmail = input("Contact Email: ")
    contactPhone = input("Contact Phone Number: ")
    orgName = input("Organization Name: ")
    primary = input(f"Is this {orgName}'s primary contact? ").lower()
    if primary == "yes":
        isPrimary = 1
    else:
        isPrimary = 0

    sqlStatement = '''INSERT INTO contacts(name, email, phone, isPrimary, organizationID) VALUES (?,?,?,?,?)'''

    cursor.execute('''SELECT id FROM organizations WHERE LOWER(name) LIKE LOWER(?)''',(f"%{orgName}%",))
    results = cursor.fetchall()
    if len(results) == 1:
        orgID = results[0][0]
        cursor.execute(sqlStatement,(contactName,contactEmail,contactPhone,isPrimary,orgID))
        conn.commit()
        print("Contact successfully added")
    elif len(results) > 1:
        print("Multiple organizations found, please choose an ID from below: ")
        i = 0
        for org in enumerate(results):
            print(f"{i+1}. {org[1]}")
        orgID = int(input("Enter the Organization ID: "))
        cursor.execute(sqlStatement,(contactName,contactEmail,contactPhone,isPrimary,orgID))
    else: 
        addOrg = input("Organization not found. Would you like to add in an organization? ")
        if "yes" in addOrg:
            newOrgID = addOrganization()
        else:
            newOrgID = None
    cursor.execute(sqlStatement,(contactName,contactEmail,contactPhone,newOrgID,isPrimary))
    conn.commit()
    conn.close()
    print("Contact successfully added!")

def searchCRM():
    conn = sqlite3.Connection("crm_database.db")
    searchParam = input("Would you like to search by contact or by organization? ").lower().strip()
    name = input("Organization or Contact Name: ")
    results = searchSomething(conn,name,searchParam)
    for row in results:
        print(f"{row}")
    conn.close()

def updateCRM():
    conn = sqlite3.Connection("crm_database.db")
    searchParam = input("Would you like to update an organization or contact? ").lower().strip()
    name = input("Name of the Organization or contact you would like to update: ")
    results = searchSomething(conn,name,searchParam)
    for row in results:
        print(f"{row}")
    

        

def searchSomething(conn,name,searchParam):
    cursor = conn.cursor()
    if "organization" in searchParam:
        sqlStatement = '''SELECT organizations.*,COUNT(contacts.id) FROM organizations LEFT JOIN contacts on organizations.id = contacts.organizationID WHERE LOWER(organizations.name) LIKE (?)'''
        cursor.execute(sqlStatement,(f"%{name}%",))
        results = cursor.fetchall()
        return(results)
    else:
        sqlStatement = '''SELECT contacts.*, organizations.name FROM contacts LEFT JOIN organizations on contacts.organizationID = organizations.id WHERE LOWER(contacts.name) LIKE (?)'''
        cursor.execute(sqlStatement,(f"%{name}%",))
        results = cursor.fetchall()
        return(results)





## main app function
database = loadData()
print(database)
while True: 
    option = input("\nWelcome to your CRM\nWhat can I help you with today? ").lower().strip()
    if "add organization" in option:
        addOrganization()
    elif "add contact" in option:
        addContacts()
    elif "search" in option:
        searchCRM()
    elif "update" in option:
        updateCRM()
    elif "exit" in option:
        break 
print("Thanks come again!")
