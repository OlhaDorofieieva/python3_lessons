# динамічний список покупок
list_products = input("Введіть назви продуктів (через пробіл): ")
temp_product = list_products.split()
print('Ваш список: ', ", ".join(temp_product))
# додавання видалення продуктів зі списку
while len(temp_product) != 0:
    product_operation = input("Введіть ознаку (+/- для додавання/видалення) та продукт. Наприклад: +молоко або -хліб: ")
    if len(product_operation) != 0:

        operation, product = product_operation[0], product_operation[1:].strip()
    # додавання продукту
        if operation == "+":
            temp_product.append(product)
            print(f'Оновлений список: {", ".join(temp_product)}')
     # видалення продукту
        elif operation == "-" and product in temp_product:
            temp_product.remove(product)
            print(f'Оновлений список: {", ".join(temp_product)}')
        elif operation == "-" and product not in temp_product:
            print("Цього продукту немає в переліку")
        else:
            print("невірна ознака")
    else:
        print("Помилка. Введіть валідні дані")
print("не містить елементів. Програма завершена.")





