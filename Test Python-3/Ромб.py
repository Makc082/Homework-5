import os 
os.system("cls")

text = input("Введіть рядок (максимум 50 символів): ")
n = len(text)

for i in range(1, n + 1):   
            print(" " * (n + 1) + text[:i])
    

for i in range(1, n):
            print(" " * (n + i) + text[i:])