# 1. შექმენი ტრანსპორტის კლასი მინიმუმ 4 კლასის პარამეტრით
# 2. დაამატე ერთი სტატიკური მეთოდი.
# 3. დაამატე ორი კლასის მეთოდი.
# 4. დაამატე __init__ magic მეთოდი და მინიმუმ 3 ობიექტის
# პარამეტრი.
# 5. დაამატე მინიმუმ 2, ობიექტის მეთოდი.
# 6. დაამატე __repr__ magic მეთოდი
# 7. ზემოხსენებული კლასისგან შექმენი მინიმუმ 5 ობიექტი და
# გამოიძახე მისი ზოგიერთი მეთოდი და პარამეტრი.
class Vehicle:
    model = "Bentley"
    warranty = "included"
    repair = "1 year"
    style = []
    # owner = ()
    def __init__(self, price, engine, wheel, year):
        self.price = price
        self.engine = engine
        self.wheel = wheel
        self.year = year

    @staticmethod
    def broken():
        print("the car need to fix its engine!")

    @classmethod
    def my_model(cls):
        print(f"The mark is {cls.model}")

    def car_features(self):
        print(f"The price of the car is {self.price}$ and\nthe year when it was produced is {self.year}")

    def car_engine(self):
        print(f"Car engine type is {self.engine}!")

    def wheel_num(self):
        print(f"Wheel number is {self.wheel}")

    def vehicle_owner(self, owner):
        self.owner = owner
        print(f"this vehicle is owned by {owner}")

    def __repr__(self):
        return (f"Above mentioned car features are: price - {self.price}$, type of engine: {self.engine},\n"
                f"number of wheels: {self.wheel} and year of production: {self.year}")


v1 = Vehicle(2000, "automatic", 4, 2020)
print(v1)
v1.broken()
v1.my_model()
v1.wheel_num()
print(v1.repair)

v2 = Vehicle(10000, "mechanic", 4, 1970)
v2.style = "retro car"
v2.model = "Chevrolet"
print(v2.style)
v2.my_model()
# ანუ წინა ხაზზე მოდელს თუ შევცვლი კლასის მეთოდში არ გადაეწერება მნიშვნელობა ხომ?
print(v2.model)
print(v2.warranty)

v3 = Vehicle(1500, "mechanic", 3, 2000)
v3.style = "motocycle"
print(f"v2 vehicle is {v2.style}, while v3 vehicle is {v3.style}")
print(f"Wheel number of the first vehicle is {v1.wheel}, while third vehicle has {v3.wheel} wheels")
v3.car_features()
print(v3)

v4 = Vehicle(20000, "automatic", 4, 2010)
v4.vehicle_owner("government")
v4.wheel_num()
v4.broken()

v5 = Vehicle(100, "mechanic", 4, 1998)
v5.vehicle_owner("factory car")
v5.car_engine()
print("the cheapest out of this vehicles is v5 and :", v5)