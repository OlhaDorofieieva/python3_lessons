#ex.1
import json
with open('departments.json', 'r') as f:
    data_depart = json.load(f)
print(f'The Departments.json file has just been loaded!')

for ki in range(len(data_depart['departments'])):
    expenses = data_depart['departments'][ki]['expenses']
    income = data_depart['departments'][ki]['income']
    #print(f' expenses = {expenses} income = {income}')
    if expenses < income:
        for ke in range(len(data_depart['departments'][ki]['employees'])):
            salary = data_depart['departments'][ki]['employees'][ke]['salary']
            data_depart['departments'][ki]['employees'][ke]['salary'] = round(salary * 1.1 ,2)

with open('new_costs.json', 'w') as write_file:
    json.dump(data_depart, write_file, indent=2)
print(f'The file new_costs.json has already been written!')


#ex.2
def print_table(number, operation):
    for i in range(1, 11):
        if operation == '*':
            result = number * i
            print(f'{number} * {i} = {result}')
        if operation == '+':
            result = number + i
            print(f'{number} + {i} = {result}')

def get_sum(number,operation):
    print_table(number, operation)
    # result_sum = sum(number + i for i in range(number + 1, number + 10))
    for i in range(number + 1, number + 10):
        number = number + i
    return number

if __name__ == '__main__':
    number = int(input("Введіть число: "))
    operation = input("Введіть операцію (* або +): ")
    # total_sum = get_sum(number, operation)
    print(f'Sum is {get_sum(number, operation)}')
