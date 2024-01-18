marta_salary = 5673.87
john_salary = 32453.44
print(marta_salary, john_salary)




john_age = 33
marta_age = 31
print("Джон:", john_age, "\n" "Марта:", marta_age)

john_name = "John"
marta_name = "Marta"
print(john_name, marta_name)

# john_gender = "man"
# marta_gender = "woman"
john_gender = False
marta_gender = True
if john_gender:
    print("John: man")
if not john_gender:
    print("-")
if marta_gender:
    print("Marta: woman")
if not marta_gender:
    print("-")

john_friends = ["Mark", "Maks", "Mark", "Bartosh", "Serg", "Mykyta", "Serg", "John"]
marta_friends = ["Yuliia", "Olha", "Gerda", "olha", "Mariia", "Karetina", "Svetlana"]

# кількість єлементів, виборка унікальних по Джону
john_list = len(john_friends)
john_friends_set = set(john_friends)
print(john_friends_set, "Кількість друзів:", john_list)

# загальний лист друзів, кількість, виборка унікальних
all_list = john_friends + marta_friends
all_len = len(all_list)
print(all_list, "Кількість імен:", all_len)
all_list_set = set(all_list)
print(all_list_set)

