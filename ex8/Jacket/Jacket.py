from python3_lessons.ex8.Top.top import Top

class Jacket(Top):  # Підклас Куртки (Верхнього Одягу)
    def __init__(self, size, color, sleeve_length, season):
        super().__init__(size, color, sleeve_length)
        self.season = season

    @property
    def wear(self):  # Реалізація методу носіння одягу
        return "Put on the jacket"

    def __repr__(self):
        return "Jacket"

    def get_print_details(self):
        return f"Jacket: Size: {self.size}, Color: {self.color}, Sleeve Length: {self.sleeve_length}, Season: {self.season}"