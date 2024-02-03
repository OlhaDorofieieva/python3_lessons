# ex1
australia_blacklist = {"John", "Katie", "Mark", "Eva"}
poker_blacklist = {"Alice", "John", "Dmytro", "Eva"}
alcohol_blacklist = {"Dmytro", "Eva", "Kate", "Olha", "Alex"}
# winner = australia_blacklist.intersection(poker_blacklist)
# winners = australia_blacklist.intersection(alcohol_blacklist)

# в одну строку
winners = australia_blacklist.intersection(poker_blacklist, alcohol_blacklist)


if not winners:
    print("Немає переможців")
else:
    print("Виграли джекпот:", winners)


# ex2
dict_names = {"Alex": "house", 'Max': 'Flat', 'Olha': 'Appartments', 'Oleh': 'Trench'}
for name, position in dict_names.items():
    print(name, "living in", position)

#[print(f'{position} is living in {dict_names[position]}') for position in dict_names]



# ex3
list1 = ['Jack', 'Leon', 'Alice', None, 32, 'Bob']

# в одну строку
# [print(f'Name is string: {el}') for el in list1 if type(el) == str]

for el in list1:
    if not type(el) == str:
        continue
    print(f'Name is: {el}')


# ex4
user_text = input("Введіть текст: ")
letter_text = {}
for el in user_text:
    if el == " ":
        continue
    count = letter_text.get(el, 0)
    letter_text[el] = count + 1
for el, count in letter_text.items():
    print(f"{el} = {count}")


#ex5
my_list = [1, 4, 2, 32, "ww", 23]
for el in my_list:
    if el is None:
        break
else:
    print("There is no None")

#ex6
user_text = input("Введіть рядок: ")
[print(f'{el} : {user_text.count(el)}') for el in set(user_text) if el != ' ']

# якщо треба виводити тільки літери
#[print(f'{el} : {user_text.count(el)}') for el in set(user_text) if el.isalfa()]
