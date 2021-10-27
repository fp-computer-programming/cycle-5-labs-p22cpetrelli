# author CJP 10/21/2021
word = input("What is your first word? ")
word2 = input("What is your second word? ")
if word == word2: 
    print(word2 + " equals " + word)
if word < word2:
    print(word + " comes before " + word2)
elif word > word2:
    print(word + " comes after " + word2)
