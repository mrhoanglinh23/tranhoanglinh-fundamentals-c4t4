import string
x = input("Enter a sentences: ")
if x=="lowercase alphabets" or "English lowercase letter" or "lowercase letters" or "alphabets":
        print(string.ascii_lowercase)


letter_count= {}
for i in x:
    if i in letter_count:
        letter_count[i] = letter_count[i] + 1
    else:
        letter_count[i] = 1

keys = letter_count.keys()
for i in sorted(keys):
    print(i, letter_count[i])