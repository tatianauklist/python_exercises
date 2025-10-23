sentence = input("Please type in a sentence: ")
word = input("Please enter the word you'd like to censor: ")

word_length = len(word)

censored_sentence = sentence.replace(word,"*"*word_length)

print(censored_sentence)