# ex.1
import time

class UserAccount:
    TOTAL_OBJECTS = 0

    def __init__(self, name, card_number, cvv, date, balance):
        UserAccount.TOTAL_OBJECTS = UserAccount.TOTAL_OBJECTS + 1
        self.card_number = card_number
        self.date = date
        self.__balance = balance # приватний атрибут
        self.name = name
        self._cvv = cvv # захищений атрибут

    def get_check_balance(self):  # function getter
        print(f"Поточний баланс - ${self.__balance}.")

    # або через @property
    # @property
    # def balance(self):  # гетер для доступу до приватного атрибута balance
    #     return self.__balance

    @classmethod  # a class method to create a total credit cards
    def total_objects(cls):
        print(f"Всього кредитних карт: {cls.TOTAL_OBJECTS}")


    @staticmethod  # a staticmethod. The method prints script start time
    def get_current_time():
        t = time.localtime()
        current_time = time.strftime("%H:%M:%S", t)
        print(f"The Script was started : {current_time}")


    def set_deposit(self, amount):  # function setter/метод для покладання грошей на рахунок
        self.__balance += amount
        print(f"${amount} додано на ваш рахунок. Новий залишок: {self.__balance} грн.")

    def withdraw(self, amount):  # метод для зняття грошей з рахунку
        if self.__balance >= amount:
            self.__balance -= amount
            print(f'Знято {amount} грн. Залишок на рахунку: {self.__balance} грн.')
        else:
            print(f'Неможливо зняти {amount} грн. Недостатньо коштів на рахунку.')

    @classmethod
    def create_account(cls, name, card_number, cvv, date, balance):  # метод для створення об'єкту класу
        return cls(name, card_number, cvv, date, balance)

    def get_print_customer_details(self):  # function getter
        print("Name:", self.name)
        print("Card Number:", self.card_number)
        print("CVV code:", self._cvv)
        print("Date of opening:", self.date)
        print(f"Balance: ${self.__balance}\n")


# Print time start of script @staticmethod
UserAccount.get_current_time()
# Input customer details
account1 = UserAccount("James Bond", 9293922345, 123, "01-01-2024", 1000)
account2 = UserAccount("Tom Hanks", 9293922346, 321, "02-01-2024", 2000)

print("Customer Details:")
account1.get_print_customer_details()
account2.get_print_customer_details()
# Print total credit cards @classmethod
account1.total_objects()
print("=============================")
account1.get_print_customer_details()
# Current __balance is $1000.
# $1000 has been deposited in your account.
account1.set_deposit(1000)
# Your current __balance $2000.
# You want to withdraw $5000
account1.withdraw(5000)
# Insufficient balance.
# The customer withdraw $1400.
account1.withdraw(1400)
account1.get_check_balance()

# ex.2

from python3_lessons.Top.top import Top
from python3_lessons.dress.dress import Dress
from python3_lessons.Jacket.Jacket import Jacket
from python3_lessons.underwear.underwear import Underwear

top1 = Top('M', 'blue', 'short',)
dress1 = Dress('L', 'red', 'short', 'casual')
jacket1 = Jacket('M', 'green', 'long','outumn')
Underwear1 = Underwear(100)
Underwear1.size = "M"
Underwear1.price = 200

print(top1.__repr__())
print(top1.get_print_details())
print(dress1.get_print_details())
print(jacket1.get_print_details())
print(Underwear1.get_print_details())
print(dress1.wear)