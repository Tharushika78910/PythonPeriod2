from car import Car

car2 = Car('ABC-123', 142)

print("\n")

car2.accelerate(30)
car2.accelerate(40)
car2.accelerate(50)
print(f"Current speed: {car2.current_speed}km/h")

car2.travelled_dist = 2000
car2.drive(1.5)
print(f"Travelled distance: {car2.travelled_dist}km")

