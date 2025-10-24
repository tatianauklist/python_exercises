print("Hello. Welcome to 'The Game'")
# Asks for name
name = input("To get started, please enter your name: ")
name_count = len(name)
index = 0
username = ""
# Would you like to play the game?
answer = input("Would you like to play the game? Y/N: ")
# yes -> loop through and create username (initials + length of name)
if answer.lower() == 'y':
    name_split = name.split()
    name_index = len(name_split) -1
    name_num = len(name_split)
    while index <= name_index:
        if name_num > 1:
            username += name_split[index][0]
            index += 1
        else:
            username += name[index]
            index += 1
    print(f"Goodbye {username.lower()}{name_count}, see you again soon")

# no -> print goodbye name, hope to see you soon
else:
    print(f"Goodbye {name}. See you again soon.")