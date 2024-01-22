# динамічний список покупок
list_products = input("Введіть назви продуктів (через пробіл): ")
product = list_products.split()
products = set(product)
temp_product = list(set(product))
if not any(temp_product):
    print("Ваш список порожній")
else:
    print(f"Ваш список: {temp_product}")
# додавання видалення продуктів зі списку
while len(temp_product) != 0:
    product_operation = input("Введіть ознаку (+/- для додавання/видалення) та продукт. Наприклад: +молоко або -хліб: ")
    operation, product = product_operation[0], product_operation[1:].strip()
    # додавання продукту
    if operation == "+" and product not in temp_product:
        temp_product.append(product)
        print(f"Оновлений список: {" ".join(temp_product)}")
    elif operation == "+" and product in temp_product:
        print("Цей продукт вже є в списку")
        # видалення продукту
    elif operation == "-" and product in temp_product:
        temp_product.remove(product)
        print(f"Оновлений список: {" ".join(temp_product)}")
    else:
        print("невірна ознака")
print("Список продуктів порожній. Програма завершена.")





