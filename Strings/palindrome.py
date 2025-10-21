word = input("Please enter a word: ")

index = -1 
backwards_word = ""
ranges = index - (len(word))

while index > ranges:
    backwards_word += word[index]+""
    index -= 1
    
if backwards_word == word:
    print(f"{word} and {backwards_word} are palindromes")
else:
    print(f"{word.title()} and {backwards_word} are NOT palindromes")