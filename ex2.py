temp = int(input("Введіть значення температурі в градусах Цельсія: "))
temp_faringejt = temp * 9/5 + 32
print(temp, "градусів Цельсія дорівнює", temp_faringejt, "градусам Фаренгейта")

temp_kelvin = temp + 273.15
print(temp, "градусів Цельсія дорівнює", temp_kelvin, "градусам Кельвіна")


number1 = input("Введіть перше число: ")
x = int(number1)
number2 = input("Введіть друге число: ")
y = int(number2)

op = input("Введіть бажану арифметичну операцію (*,/,+,-): ")
if op == "*":
    print ("Добуток дорівнює:", (x * y))
elif op == "/":
    if y == 0:
        k = int(input("Введіть число відмінне від нуля: "))
        print ("Частка дорівнює: ", (x / k))
    else: print("Частка дорівнює: ", (x / y))
elif op == "+":
    print("Сума дорівнює:", (x + y))
elif op == "-":
    print("Різниця дорівнює: ", (x - y))
else:
    print("Невідома операція")