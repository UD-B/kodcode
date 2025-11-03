class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    def get_car_info(self):
        return f"make: {self.make}, model: {self.model}, year: {self.year}."

new_car = Car("toyota", "4runner", "2026")
print("make", new_car.make)
print("model", new_car.model)
print("year", new_car.year)
print("car info", new_car.get_car_info())
new_car.color = "white"
print("car color", new_car.color)
del new_car.color