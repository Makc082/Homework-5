

text = input("Enter your text: ").lower()

spam_words = [
    "кредит", "швидке схвалення", "готівка", "знижка", "розпродаж", "виграш", 
    "viagra", "схуднення", "найкращий продукт", "легкий заробіток", "без ризику", 
    "швидкі гроші", "виграй гроші", "гроші за реєстрацію", "легко і швидко", 
    "терміново", "тільки сьогодні", "суперпропозиція", "не втратьте шанс", 
    "подарунки для вас", "нові знижки"
]

words = text.split()

is_spam = False

for word in words:
    if word in spam_words:
        is_spam = True
        break

if is_spam == True:
    print("This is SPAM!")
else:
    print(text)