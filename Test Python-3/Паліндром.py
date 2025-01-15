text = input("Enter your text: ")

clean_text = ""

for char in text:
    if char.isalpha():
        clean_text += char.lower()

x = clean_text
y = clean_text[::-1]

if x == y:
    print("Palindrome!")
else:
    print("Not palindrome!")