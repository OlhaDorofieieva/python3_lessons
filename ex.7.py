print("Ex.1")
# Виправлене завдання
def print_name_func_decorator(func):
    def wrapper(*args, **kwargs):
        print("*" * 15)
        print(f'Function name is {func.__name__}')
        return func(*args, **kwargs)
    return wrapper

@print_name_func_decorator
def my_sum(num1, num2):
    return num1 + num2

@print_name_func_decorator
def my_multiple(num1, num2):
    return num1 * num2

if __name__ == '__main__':
    result1 = my_sum(33, 444)
    print(f'Сума двох чисел дорівнює', result1)
    result2 = my_multiple(33, 444)
    print(f'Частка двох чисел дорівнює', result2)

print("Ex.2")
# Створіть функцію, яка може друкувати квадрати парних чисел у діапазоні від 0 до 1000000000 включно

def my_generator(n: int) -> int:
    value = 0
    while value < n:
        yield value ** 2
        value += 2

# next step generator
for value in my_generator(20):  # If prod then my_generator(1000000000)
    # print each value
    print(value)


print("Ex.3")
# Створіть декоратор, який повертає результат функції. а також час за який вона виконана.
import time

def print_time_func_exec(function):
    def wrapper(nums):
        current_time = time.time()
        print("-" * 15)
        print(f'sum_fibonacci_numbers {nums} = {sum(function(nums))}')
        print(f'time spent = {round(time.time() - current_time, 2)} sec')
        print("-" * 15)
    return wrapper

@print_time_func_exec
def fibonacci_sum_numbers(nums):  # використовуємо генератор для сум чисел
    x, y = 0, 1
    for _ in range(nums):
        x, y = y, x + y
        yield x

if __name__ == '__main__':
    fibonacci_sum_numbers(5000)

print("Ex.4")
# Створіть функцію котра буде повертати число фібоначі, на вхід функція приймає номер в послідовності Фібоначі. Використовуйте рекурсію.

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

n = int(input("Введіть номер числа з послідовності Фібоначчі: "))
print("Число Фібоначчі з номером", n, "дорівнює", fibonacci(n))

