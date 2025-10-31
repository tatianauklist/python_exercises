import json
import sqlite3


def loadData():
    sqlite3Connection = sqlite3.Connection("crm_database.db")
    cursor = sqlite3Connection.cursor()
    cursor.execute('''
        CREATE IF NOT EXISTS organizations(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            industry TEXT NOT NULL,
            website TEXT,
            notes TEXT
                   )
    ''' )
    cursor.execute(''' 
        CREATE IF NOT EXISTS contacts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE,
            phone TEXT,
            originizationID INTEGER,
            FOREIGN KEY originzationID REFERENCES orginizations(id)          
            )               
    ''')
    sqlite3Connection.commit()
    sqlite3Connection.close()
    return("Database Initiated")
    
    

###def addOrganization():

###def addContacts():

###def deleteOrganization():

###def deleteContact():

###def updateContact():

###def searchCRM():


    




## menu 
database = loadData()
print(database)
print("\nWelcome to your CRM\nWhat can I help you with today? ")
database = loadData()
print(database)
