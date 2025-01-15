email = input("Enter your email: ")

x = email.find("@")
y = email.find(".")

if x != 0 and x != len(email) - 1:
    if y != 0 and y != len(email) - 1:
        print("Email is correct!")
    else:
        print("Email is not correct")
