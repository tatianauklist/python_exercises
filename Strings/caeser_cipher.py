# Constants and message
main_message = input("What message would you like to encode?: ")
shift = int(input("What would you like to shift your message by? "))
constant_alpha = "abcdefghijklmnopqrstuvwxyz"
message_len = (len(main_message) -1)
upper_index = (len(constant_alpha) - 1)
index = 0
encrypted_message = ""

# Set loop length
while message_len >= index:
# Checks to see if the index is space
    if main_message[index] == " ":
        encrypted_message += " "
# If not, checks to find the new index
    else:
        og_index = constant_alpha.find(main_message[index])
        new_index = og_index + shift
# If the new index is higher than the alphabet, this reset it
        if new_index > upper_index:
            new_index = new_index - upper_index - 1
            encrypted_message += constant_alpha[new_index]
        else:
            encrypted_message += constant_alpha[new_index]
# Changes the index
    index += 1
print(f"'{main_message}' encrypted is '{encrypted_message}'")
               
        






      
