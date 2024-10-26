from car import Car

car2 = Car('ABC-123', 142)

print(f"""
Registration number {car2.registration_num}
Maximum speed {car2.maximum_speed}
Current speed {car2.current_speed}
Travelled distance {car2.travelled_dist}""")

print("\n")
car2.accelerate(30)
car2.accelerate(70)
car2.accelerate(50)

car2.accelerate(-200)
print(f"Current speed: {car2.current_speed}km/h")