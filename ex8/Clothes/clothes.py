from abc import ABC, abstractmethod

class Clothes(ABC):  # Клас Одягу (абстрактний)
    size = None
    color = "Black"
    # def __init__(self, size, color):
    #     self.size = size
    #     self.color = color

    @abstractmethod
    def wear(self):  # Абстрактний метод для носіння одягу
        pass

    @classmethod
    @property
    def get_class_name(cls):  # Повертає ім'я класу
        return cls.__name__

    @abstractmethod
    def get_print_details(self):
        pass

