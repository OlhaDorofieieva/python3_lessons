from python3_lessons.Clothes.clothes import Clothes

class Underwear(Clothes):  # Підклас нижнього одягу
    def __init__(self, price):
        self.__price = price #інкапсуляція

    @property
    def wear(self):  # Реалізація методу носіння одягу
        return "Put on the underwear"

    def __repr__(self):
        return "Underwear"

    def get_print_details(self):
        return f"Underwear: Size: {self.size}, Color: {self.color}, Price: {self.__price}"