import random
import string

password_length = int(input("Enter password length: "))

symbols = string.ascii_letters + string.digits + string.punctuation
print("Your password: ", end="")

for i in range(password_length):
    password = random.choice(symbols)
    print(password, end="")
    