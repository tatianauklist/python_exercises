#ask for input
# import string
from array import *
sentence = input("Please type in a sentence: ")


# index = array('i',sentence.find(string.punctuation))
# print(index)



# loop to replace punctuations
#if sentence[index] not in string.punctuation:
#    sentence = sentence[index].replace(string.punctuation,'')
#    print(sentence)
    
# split the sentence
split_sentence = sentence.split()
word_count = len(split_sentence)
# print(split_sentence)

#print results
print(f"The sentence '{sentence}' contains {word_count} words.")

