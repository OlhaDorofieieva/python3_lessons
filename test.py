#ex.2
from abc import ABC, abstractmethod

# абстракція
class Transport(ABC):
    max_speed = None
    model = None
    long = None

    @abstractmethod
    def move(self):
        pass

    @classmethod
    @property
    def get_class_name(cls):
        return cls.__name__

class Water_Transport(Transport): # наслідування

    def __init__(self, model: str, max_speed: int, color: str = None) -> None:
        self.max_speed = max_speed
        self.model = model
        if color is None:  # "Default constructor called"
            self.color = 'neutral'  # color does not matter
        else:
            self.color = color  # "Parameterized constructor called with color"

    @property
    def move(self):
        return "Sailing"

    def __repr__(self):  # additional class description
        return "Water_Transport_class_Transport"

class Boat(Water_Transport): # наслідування
    def __init__(self, model, max_speed, color, price):
        super().__init__(model, max_speed, color) # Вызываем конструктор родительского класса
        self.price = price
        pass

    @property
    def move(self):
        return super().move + ' and Swimming'
class Cround_Transport(Transport): # наслідування
    def __init__(self, engine):
        self.__engine = engine # інкапсуляція

    @property
    def get_engine(self):
        return self.__engine # інкапсуляція

    @property
    def move(self):
        return "Driving"

    def __repr__(self):  # additional class description
        return 'Cround_Transport is child class'

e1 = Water_Transport(model='Fiat', max_speed=200) # поліморфізм
print(e1.__repr__())
print(e1.model, e1.max_speed, e1.long, e1.color, e1.move)

e12 = Cround_Transport(engine='diesel')
e12.long = 232322
print(e12.get_engine, e12.long, e12.model, e12.move, e12.max_speed)
print(e12.__repr__())
print(e12.get_class_name)

boat1= Boat('BMW', 300, None, 10000) # поліморфізм
print(boat1.move)
print(boat1.model, boat1.max_speed, boat1.color, boat1.price, boat1.long)

