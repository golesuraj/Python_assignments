sentence = input("Enter a sentence: ")
word = input("Enter word: ")
if word in sentence.split():
    print("Found")
else:
    print("Not found")
