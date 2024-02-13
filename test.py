print("Ex.1")
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
    print(f'You numbers is {num1} and {num2}')
    return num1 * num2

if __name__ == '__main__':
    result1 = my_sum(33, 444)
    print(f'Сума двох чисел дорівнює', result1)
    result2 = my_multiple(33, 444)
    print(f'Частка двох чисел дорівнює', result2)

