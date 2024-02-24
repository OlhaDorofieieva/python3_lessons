from python3_lessons.Clothes.clothes import Clothes

class Dress(Clothes):  # Підклас Верхнього Одягу
    def __init__(self, size, color, length, style):
        self.length = length
        self.style = style
        self.size = size
        self.color = color

    @property
    def wear(self):  # Реалізація методу носіння одягу
        return "Put on the dress"

    def __repr__(self):
        return "Dress"

    def get_print_details(self):
        return f"Dress: Size: {self.size}, Color: {self.color}, Length: {self.length}, style: {self.style}"