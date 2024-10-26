from elev import Elevator

target_floor = int(input("Which floor do you want to go? "))

elevator1 = Elevator(1, 10)
elevator1.go_to_floor(target_floor)
print("\n")
elevator1.go_to_floor(elevator1.bottom)
