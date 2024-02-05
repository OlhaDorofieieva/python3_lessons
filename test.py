import json
with open(department.json, "r") as f:
    data = json.load(f)



def increase_salary(department):
    if department["expenses"] < department["income"]:
        for employees in department["employees"]:
            employees["salary"] *= 1.1  # Збільшуємо зарплату на 10%




with open('new_costs.json', 'w') as write_file:
    json.dump(data_depart, write_file, indent=2)
    print(f'The file new_costs.json has already been written!')

if __name__ == "__main__":
    main()

