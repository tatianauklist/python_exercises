email = input("Please input your email: ")
username = ""
index = 0

while email[index] != '@':
    username += email[index]
    index += 1
print(f"Your username is {username}")