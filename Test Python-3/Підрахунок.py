import string

text = input("Enter your text: ")

clean_text = text.translate(str.maketrans('', '', string.punctuation))

x = clean_text.split()
y = len(x)
z = 0

for i in x:
    z += len(i)

if y > 0:
    a = z // y
    print(f"Average word length: {a}")
