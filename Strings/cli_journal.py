# Libraries
import datetime

def main_menu():
    print("Main Menu")
    print("Please select your option from the following menu below.")
    print("1. Write a new journal entry\n2.View all journal entries\n3.Search all journal entries\n4. Exit")
def writeNewJournal ():
    journalEntry = input("What's on your mind: ")
    date = datetime.datetime.now()
    journalEntry = f"{date}: {journalEntry}"
    f = open("myjournal.txt","a")
    with open("myjournal.txt","a") as f:
        f.write(journalEntry + "\n")
        f.close()
def viewAllEntries():
    with open("myjournal.txt","r") as f:
        print(f.read())
        f.close()
def searchEntries():
    search = input("What would you like to look for? ")
    index = 0
    with open("myjournal.txt","r") as f:
        for line in f:
            line = line.rstrip()
            if line.find(search) == -1:
                continue
            print(line)
    f.close()



# Welcome menu
print("Welcome to your Journal\n")
input("Press Enter to continue on to the main menu\n")
# Main menu
main_menu()
while True:
    choice = int(input("What would you like to do today? "))

    # Write new journal
    if choice == 1:
        writeNewJournal()
    elif choice == 2:
        viewAllEntries()
    elif choice == 3:
        searchEntries()
    else:
        break


