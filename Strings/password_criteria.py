password_length = 8
total = 0

password = input("Please enter a password: ")
pass_length = len(password)
print(pass_length)

while pass_length >= 1 and total <= 3:
    if pass_length >= password_length:
        total += 1
        print(f"Your password meets the criteria of being at least {password_length} characters long")
    else:
        print(f"Your password does not meet the criteria of being at least {password_length}")
    if any(map(str.isupper,password)):
        total += 1
        print(f"Your password has met the criteria of having at least one upper case letter")
    else: 
        print("Your password does not meet the criteria of having at least one upper case letter")
    if any(map(str.islower,password)):
        total += 1
        print("Your password meets the criteria of having at least one lower case character")
    else:
        print("Your password has not met the criteria of having at least one lower case character")
    break

if total == 3:
    print("Congratulations! Your password is strong enough")
else:
    print(f"Your password only met {total} of the 3 checks. Please try again")
    
    
