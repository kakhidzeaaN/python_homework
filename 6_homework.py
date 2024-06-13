# 1. შექმენი ქვეყნის აბსტრაქტული კლასი. რომელსაც
# ექნება მინიმუმ სამი აბსტრაქტული მეთოდი.
# 2. შექმენი მისგან საქართველოს კლასი, რომელსაც ექნება
# public, protected და private ცვლადები (მაგალითად
# ბიუჯეტი, მოსახლეობა და ა.შ.).
# 3. შექმენი საქართველოს ობიექტი და გამოიყენე
# ზემოხსენებული მეთოდები.

from abc import ABC, abstractmethod


class Country(ABC):
    @abstractmethod
    def location(self):
        pass

    @abstractmethod
    def get_area(self):
        pass

    @abstractmethod
    def get_budget(self):
        pass


class Georgia(Country):
    def __init__(self):
        self._population = "this is protected attribute"
        self.__religion = "This is private attribute"
        self.language = "georgian"

    def location(self):
        print("Georgia is located in Europe")
        # print("The population of Georgia is 3.4 billion people!")

    def get_area(self):
        print("The area of georgia is 57700 squared meter")

    def get_budget(self):
        while True:
            try:
                num = int(input("Enter your desired number here:\n"))
                print(f"The budget of georgia is {num} lari")
                break
            except:
                print("Please enter the number")


grg = Georgia()
print("general attribute is accessible easily:",grg.language)
print(grg._population)
grg._population = "The population of Georgia is 3.4 billion people!"
print("protected attribute has changed:",grg._population)
grg.location()
grg.get_area()
grg.get_budget()
