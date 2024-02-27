class Train:
    def __init__(self, train_number):
        self.train_number = train_number
        self.locomotive = None  # Локомотив поки не визначений
        self.wagons = []

    def add_wagon(self, wagon):
        if len(self.wagons) < 12:  # Перевіряємо, що додаємо не більше 12 вагонів
            self.wagons.append(wagon)
        else:
            print(f' Не можемо додати більше вагонів, максимальний ліміт = 12')

    def __str__(self):
        return f"Потяг {self.train_number} налічує {len(self.wagons)} вагонів."


class Wagon:
    max_passengers = 10
    def __init__(self, wagon_number):
        self.wagon_number = wagon_number
        self.passengers = []

    def add_passenger(self, passenger):
        if len(self.passengers) >= self.max_passengers:
            print(f"Пасажир не може бути доданий до переліку, максимальний ліміт = {self.max_passengers}.")
            return

        if passenger in self.passengers:
            print(f"Пасажир {passenger} вже є у переліку.")
            return

        self.passengers.append(passenger)
        print(f"Пасажир {passenger} доданий до переліку у {self.wagon_number}.")

    def remove_passenger(self, passenger):
        if passenger in self.passengers:
            self.passengers.remove(passenger)
            print(f"{passenger} видалений з переліку пасажирів {self.wagon_number}.")
        else:
            print(f"{passenger} не може бути видалений, пассажира немає у переліку.")

    def __str__(self):
        return f"{self.wagon_number} з {len(self.passengers)} пасажирами."

    def __len__(self):
        return len(self.passengers)

class Locomotive:
    def __init__(self, wagon_number, driver):
        self.locomotive = Wagon(wagon_number)
        self.driver = driver

    def __str__(self):
        return f"{self.locomotive.wagon_number} (Локомотив) за кермом: {self.driver}"

    def add_driver(self, driver):
        self.driver = driver

    def remove_driver(self):
        self.driver = None


# Створюємо потяг
train = Train("Warszawa-Kiyv")

# Додаємо вагони
for i in range(13):  # Намагаємося додати 13 вагонів
    wagon = Wagon(f"Вагон {i + 1}")
    train.add_wagon(wagon)
# Створюємо локомотив
locomotive = Locomotive("HEAD", "John")
train.locomotive = locomotive

# Знаходимо п'ятий вагон в потязі
wagon_5 = train.wagons[4]
wagon_5.add_passenger("Tom Hanks")
wagon_5.add_passenger("James Bond")
# Знаходимо перший вагон в потягу
wagon_1 = train.wagons[0]
wagon_1.add_passenger("Olha")
wagon_1.add_passenger("Maya")
wagon_1.add_passenger("Nata")
# Видаляємо пасажирів з першого вагону
wagon_1.remove_passenger("Olha")
wagon_1.remove_passenger("Olha")
wagon_1.remove_passenger("Nata")
wagon_1.remove_passenger("Tom")


# Виводимо інформацію про потяг
print(train)
print(train.locomotive)
for wagon in train.wagons:
    print(wagon)
