text = input("Enter a paragraph or sentence: ")

cleaned_text = " ".join(text.split())

total_chars = len(text)
words = cleaned_text.split()
total_words = len(words)

total_sentences = text.count(".") + text.count("!") + text.count("?")
if total_sentences == 0 and total_words > 0:
    total_sentences = 1

vowels = "aeiouAEIOU"
vowel_count = 0
consonant_count = 0
digit_count = 0
special_count = 0

for ch in text:
    if ch in vowels:
        vowel_count += 1
    elif ch.isalpha():
        consonant_count += 1
    elif ch.isdigit():
        digit_count += 1
    elif not ch.isspace():
        special_count += 1

print("\n--- Text Analysis Results ---")
print("Cleaned Text:", cleaned_text)
print("Total Characters:", total_chars)
print("Total Words:", total_words)
print("Total Sentences:", total_sentences)
print("Vowels:", vowel_count)
print("Consonants:", consonant_count)
print("Digits:", digit_count)
print("Special Characters:", special_count)

print("Uppercase:", text.upper())
print("Lowercase:", text.lower())

search_word = input("\nEnter a word to search: ")
found = False
for w in words:
    if w.lower() == search_word.lower():
        found = True
        break

if found:
    print("The word exists in the text.")
else:
    print("The word does not exist in the text.")

print("\nWord Frequency:")
counted_words = []
for w in words:
    lower_w = w.lower()
    if lower_w not in counted_words:
        count = 0
        for item in words:
            if item.lower() == lower_w:
                count += 1
        print(w, ":", count)
        counted_words.append(lower_w)
