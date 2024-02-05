# import json
#
# def increase_salary(department):
#     if department["expenses"] < department["income"]:
#         for employees in department["employees"]:
#             employees["salary"] *= 1.1  # Збільшуємо зарплату на 10%
#
# def process_departments(data):
#     for department in data["departments"]:
#         increase_salary(department)
#
# def main():
#     input_filename = "departments.json"
#     output_filename = "new_costs.json"
#
#     with open(input_filename, "r") as file:
#         data = json.load(file)
#
#     process_departments(data)
#
#     with open(output_filename, "w") as file:
#         json.dump(data, file, indent=2)
#
# if __name__ == "__main__":
#     main()
#

def print_table(num, operation):
    print(f'Table for {num} {operation}:')
    for i in range(1, 11):
        result = num * i
        print(f'{num} {operation} {i} = {result}')

def get_sum(num, operation):
    print_table(num, operation)
    # Розрахунок суми для чисел від 6 до 15 (включно)
    result_sum = sum(num * i for i in range(6, 16))
    return result_sum

if __name__ == '__main__':
    num = int(input('Enter a number: '))
    operation = input('Enter an operation (+ or *): ')

    if operation not in ('+', '*'):
        print('Invalid operation. Please enter + or *.')
    else:
        total_sum = get_sum(num, operation)
        print(f'Sum is {total_sum}')