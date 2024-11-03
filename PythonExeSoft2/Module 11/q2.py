from car import Car

class ElectricCar(Car):
    def __init__(self,regPlate, maxSpeed, battery_capacity):
        super().__init__(regPlate, maxSpeed)
        self.battery_capacity = battery_capacity

    def print_odometer(self):
        print("Odometer: " + str(self.odometer))


class GasolineCar(Car):
    def __init__(self, regPlate, maxSpeed, tank_capacity):
        super().__init__(regPlate, maxSpeed)
        self.tank_capacity = tank_capacity

    def print_odometer(self):
        print("Odometer: " + str(self.odometer))

el_car1 = ElectricCar("ABC-15",180, 60.5)
gas_car1 = GasolineCar("ACD-40", 175, 35)
el_car1.accelerate(30.)
gas_car1.accelerate(30.)
el_car1.drive(3.);gas_car1.drive(3.)
el_car1.print_odometer();gas_car1.print_odometer()