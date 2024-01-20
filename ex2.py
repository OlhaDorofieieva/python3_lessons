temp = int(input("Введіть значення температурі в градусах Цельсія: "))
temp_faringejt = temp * 9/5 + 32
print(temp, "градусів Цельсія дорівнює", temp_faringejt, "градусам Фаренгейта")

temp_kelvin = temp + 273.15
print(temp, "градусів Цельсія дорівнює", temp_kelvin, "градусам Кельвіна")


num_1 = int(input("Введіть перше число: "))
num_2 = int(input("Введіть друге число: "))

op = input("Введіть бажану арифметичну операцію (*,/,+,-): ")
if op == "*":
    print("Добуток дорівнює:", (num_1 * num_2))
elif op == "/":
    if num_2 == 0:
       # k = int(input("Введіть число відмінне від нуля: "))
        print("Не можна ділити на 0")
    else: print("Частка дорівнює: ", (num_1 / num_2))
elif op == "+":
    print("Сума дорівнює:", (num_1 + num_2))
elif op == "-":
    print("Різниця дорівнює: ", (num_1 - num_2))
else:
    print("Невідома операція")