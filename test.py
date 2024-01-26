user_text = input("Введіть рядок: ")
#print(Counter(char for char in user_input if char.isalpha()))

[print(f'{el} : {user_text.count(el)}') for el in set(user_text) if el.isalfa()]