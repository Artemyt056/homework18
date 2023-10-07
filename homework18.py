class Car:
    def __init__(self, producer, brand, graduation_year=2020, run=0, fuel_consumption=0.0):
        self.producer = producer
        self.brand = brand
        self.graduation_year = graduation_year
        self.run = run
        self.fuel_consumption = fuel_consumption

    def __str__(self):
        return f"Car: {self.producer} {self.brand}, graduation_year: {self.graduation_year}, Run: {self.run} km, fuel_consumption: {self.fuel_consumption} l/100km"


car1 = Car("Toyota", "Camry", 2021, 15000, 7.5)
car2 = Car("Honda", "Civic", 2019, 20000, 6.8)
car3 = Car("Ford", "Focus", 2020, 10000, 8.2)

print(car1)
print(car2)
print(car3)
