import random 

password_length = int(input("Enter lenght password: "))

digits = "0123456789"
lowercase = "abcdefghijklmnopqrstuvwxyz"
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
symbols = "!@#$%^&*()"

total_symbols = digits + lowercase + uppercase + symbols

password = ""
for _ in range(password_length):
    random_index = random.randint(0, len(total_symbols) - 1)
    password += total_symbols[random_index]

print(f"Your password: {password}")
