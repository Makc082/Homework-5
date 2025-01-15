import string

text = input("Enter your text: ").strip()

total_characters = len(text)
vowels = "aeiouAEIOUаеєиіїоуюяАЕЄИІЇОУЮЯ" 
consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZбвгґджзйклмнпрстфхцчшщБВГҐДЖЗЙКЛМНПРСТФХЦЧШЩ"

total_vowels = 0
total_consonants = 0
total_punctuation = 0
total_digits = 0
total_other_symbols = 0

words = text.split()
total_words = len(words)

for char in text:
    if char in vowels:
        total_vowels += 1
    elif char in consonants:
        total_consonants += 1
    elif char in string.punctuation:
        total_punctuation += 1
    elif char.isdigit():
        total_digits += 1
    elif not char.isspace():
        total_other_symbols += 1

print(f"""В текті всього символів: {total_characters}
Слів: {total_words}
Голосніх: {total_vowels}
Приголосних: {total_consonants}
Знаків пунктуації: {total_punctuation}
Цифер: {total_digits}
Інших символів: {total_other_symbols}""")