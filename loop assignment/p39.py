s = input("Enter a string: ")
words = s.split()
count = 0
for _ in words:
    count += 1
print("Total words:", count)
