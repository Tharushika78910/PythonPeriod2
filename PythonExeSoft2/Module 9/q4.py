from car import Car
from prettytable import PrettyTable
import random

def add_cars(num_cars):
    cars_list = []
    for i in range(1, num_cars+1):
        registration_number = f"ABC-{i}"
        max_speed = random.randint(100,200)
        cars_list.append(Car(registration_number, max_speed))
    return cars_list

def car_race(cars_list):
    winner1 = None
    while not winner1:
        for car in cars_list:
            speed_change = random.randint(-10,15)
            car.accelerate(speed_change)

            car.drive(1)

        for car in cars_list:
            if car.travelled_dist >= 10000:
                winner1 = car
                break

    return winner1

def display_cars(cars_list):
    table=PrettyTable()
    table.field_names = ["Registration no. of the car", "Maximum speed", "Travelled distance"]
    for car in cars_list:
        table.add_row([car.registration_num, car.maximum_speed, car.travelled_dist])
    print(table)

cars = add_cars(10)
winner = car_race(cars)
display_cars(cars)
