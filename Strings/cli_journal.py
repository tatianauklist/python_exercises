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
    else:
        break


