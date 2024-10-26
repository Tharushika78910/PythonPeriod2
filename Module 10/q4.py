import random
from prettytable import PrettyTable
from cars import Car

class Race:
    def __init__(self, name, distance, cars):
        self.name = name
        self.distance = distance
        self.cars = cars

    def hours_passed(self):
        for car in self.cars:
            car.accelerate(random.randint(-10,15))
            car.drive(1)

    def print_status(self):
        table = PrettyTable()
        table.field_names = ["Registration no. of the car", "Maximum speed", "Travelled distance"]
        for car in self.cars:
            table.add_row([car.registration_num, car.maximum_speed, car.travelled_dist])
        print(table)

    def race_finished(self):
        for car in self.cars:
            if car.travelled_dist >= self.distance:
                return True
            return False

cars = []
for i in range(10):
    cars.append(Car("ABC - "+str(i+1), random.randint(100, 200)))

race = Race("Grand Demolition Derby", 8000, cars)
n = 0
while not race.race_finished():
    race.hours_passed()
    n=n+1
    if n%10==0:
        print(f"After {n} hours.")
        race.print_status()

print(f"Final results after {n} hours.")
race.print_status()