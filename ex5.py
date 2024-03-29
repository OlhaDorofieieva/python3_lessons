# ex.1
str_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

dict_list = dict(map(lambda x: (int(x), int(x) ** 2), str_list))
print(dict_list)

#ex.2

class WrongOperatorError(Exception):
    pass
class FormulaError(Exception):
    pass

num_try = 0
while num_try < 3:
    try:
        formula = input("Введіть формулу з чисел та оператора, розділених пробілом. (Наприклад: 2 * 3): ")
        user_op = formula.split()
        if len(user_op) != 3:
            raise FormulaError('Введіть формулу, розділену пробілами')

        num1 = float(user_op[0])
        num2 = float(user_op[2])
        op = user_op[1]
        if op not in ('*','/'):
            raise WrongOperatorError("Допустимі тільки оператори '*' та '/'")

        if op == '/' and num2 == 0:
            raise ZeroDivisionError('На нуль ділити не можна')

        if op == '*': print(f'result = {round((num1 * num2), 2)}')
        if op == '/': print(f'result = {round((num1 / num2), 2)}')
        break

    except WrongOperatorError as mess:
        num_try +=1
        print(mess)
    except FormulaError as mess:
        num_try += 1
        print(mess)
    except ValueError:
        print('Некорректне число. Спробуйте ще раз')
        num_try += 1
    except ZeroDivisionError as mess:
        num_try += 1
        print(mess)
    finally:
        if num_try == 3:
            print('Закінчилися спроби. Програма завершена')



