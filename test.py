class FormulaError(Exception):
    pass

class WrongOperatorError(FormulaError):
    pass

def calculate_formula(formula):
    try:
        parts = formula.split()
        if len(parts) != 3:
            raise FormulaError("Формула повинна складатися з трьох елементів")

        num1 = float(parts[0])
        operator = parts[1]
        num2 = float(parts[2])

        if operator not in ('*', '/'):
            raise WrongOperatorError("Допустимі тільки оператори '*' та '/'")

        if operator == '/' and num2 == 0:
            raise ZeroDivisionError("Ділення на нуль неможливе")

        result = num1 * num2 if operator == '*' else num1 / num2
        return round(result, 2)

    except ValueError as ve:
        raise FormulaError(f"Помилка при конвертації у число: {ve}")
    except FormulaError as fe:
        raise fe
    except Exception as e:
        raise FormulaError(f"Невідома помилка: {e}")

# Три спроби скористуватись калькулятором
for _ in range(3):
    try:
        user_input = input("Введіть формулу (наприклад, 2 * 5): ")
        result = calculate_formula(user_input)
        print(f"Результат: {result}")
        break  # Якщо все введено правильно, виходимо з циклу
    except FormulaError as fe:
        print(f"Помилка: {fe}")
    except Exception as e:
        print(f"Невідома помилка: {e}")
else:
    print("Закінчились спроби. Програма завершилась.")