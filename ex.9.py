class Train:
    def __init__(self, train_number):
        self.train_number = train_number
        self.locomotive = Wagon("HEAD")  # Локомотив завжди є, і в нього нікого не посадиш
        self.wagons = []

    def add_wagon(self, wagon):
        if len(self.wagons) < 12:  # Перевіряємо, що додаємо не більше 12 вагонів
            self.wagons.append(wagon)
        else:
            print(f' Не можемо додати більше вагонів, maximum limit = 12')

    def __str__(self):
        return f"Потяг {self.train_number} налічує {len(self.wagons)} вагонів."


class Wagon:
    max_passengers = 10
    def __init__(self, wagon_number):
        self.wagon_number = wagon_number
        self.passengers = []

    def add_passenger(self, passenger):
        if len(self.passengers) < self.max_passengers:  #Умова, що пассажирів в вагоні не більше 10
            if passenger not in self.passengers:  #Перевіряємо, що цього пасажиру немає в переліку
                self.passengers.append(passenger)
                print(f"Пасажир {passenger} доданий до переліку у {self.wagon_number}.")
            else:
                print(f"Пасажир {passenger} вже є у переліку.")
        else:
            print("Пасажир не може бути доданий до переліку, maximum limit = 10.")

    def remove_passenger(self, passenger):
        if passenger in self.passengers:
            self.passengers.remove(passenger)
            print(f"{passenger} видалений з переліку пасажирів вагона {self.wagon_number}.")
        else:
            print(f"{passenger} не може бути видалений, його немає у переліку пасажирів.")

    def __str__(self):
        return f"{self.wagon_number} з {len(self.passengers)} пасажирами."

    def __len__(self):
        return len(self.passengers)

# Створюємо потяг
train = Train("Warszawa-Kiyv")

# Додаємо вагони
for i in range(13):  # Намагаємося додати 13 вагонів
    # carriage = Carriage(i + 1)
    wagon = Wagon(f"Вагон {i + 1}")
    train.add_wagon(wagon)

# Знаходимо п'ятий вагон в потязі
wagon_5 = train.wagons[4]
wagon_5.add_passenger("Tom Hanks")
wagon_5.add_passenger("James Bond")
# Знаходимо перший вагон в потязі
wagon_1 = train.wagons[0]
wagon_1.add_passenger("Olha")
wagon_1.add_passenger("Maya")
wagon_1.add_passenger("Nata")
# Видаляємо пасажирів з першого вагону
wagon_1.remove_passenger("Olha")
wagon_1.remove_passenger("Olha")
wagon_1.remove_passenger("Nata")
wagon_1.remove_passenger("Tom")


# train.wagons[4].add_passenger("Passenger 1") запис в одну строку
# train.wagons[4].remove_passenger("Passenger 1")

# Виводимо інфу про потяг
print(train)
print(train.locomotive)
for wagon in train.wagons:
    print(wagon)
# print(f'-{wagon.wagon_number}: {len(wagon)} пасажирів') # або :))

print(f'<=[{train.locomotive.wagon_number}]', end='')
for wagon in train.wagons:
    # print(wagon)
    print(f'-[{wagon.wagon_number}]', end='')
