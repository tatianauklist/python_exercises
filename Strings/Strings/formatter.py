name = input("Please input your full name: ")
name = name.title()
splits = name.split()
number_of_names = len(splits)
index = 0
upper = name.upper()
lower = name.lower()

char_count = len(name) - name.count(' ')

if number_of_names > 1:
    first_initial = splits[index][0]
    index += 1
    last_initial = splits[index][0]
    print(f"Your Initials Are: {first_initial}{last_initial}")
else:
    initial = splits[index][0]
    print(f"Your Initials Are: {initial}")




print(f"Upper: {upper}")
print(f"Lower Case: {lower}")
print(f"Character count: {char_count}")