from python3_lessons.Clothes.clothes import Clothes

class Top(Clothes):  # Підклас Верхнього Одягу
    def __init__(self, size, color, sleeve_length):
        self.sleeve_length = sleeve_length
        self.size = size
        self.color = color

    @property
    def wear(self):  # Реалізація методу носіння одягу
        return "Put on the top"

    def __repr__(self):
        return "Top"

    def get_print_details(self):
        return f"Top: Size: {self.size}, Color: {self.color}, Sleeve Length: {self.sleeve_length}"