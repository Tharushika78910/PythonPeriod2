class Elevator:
    def __init__(self, bottom, top):
        self.bottom = bottom
        self.top = top
        self.current = bottom

    def floor_up(self):
        if self.current < self.top:
            print(f"Elevator is going to floor up from {self.current} to {self.current + 1}")
            self.current += 1
            return True
        else:
            return False

    def floor_down(self):
        if self.current > self.bottom:
            print(f"Elevator is going to floor down from {self.current} to {self.current - 1}")
            self.current -= 1
            return True
        else:
            return False

    def go_to_floor(self, floor):
        if floor > self.top or floor < self.bottom:
            print("Invalid floor.")
            print(f"This elevator is going from {self.bottom} to {self.top} only.")
            return

        print(f"Elevator is in floor: {self.current} and going to floor: {floor}.")
        while self.current < floor:
            self.floor_up()

        while self.current > floor:
            self.floor_down()

        print(f"Elevator is in {floor}th floor.")

class Building:
    def __init__(self, bottom, top, elevators):
        self.elevators = []
        for i in range(elevators):
            self.elevators.append(Elevator(bottom, top))

    def run_elevator(self, elevator_num, floor):
        print(f"Elevator {elevator_num} is moving.")
        self.elevators[elevator_num - 1].go_to_floor(floor)

    def fire_alarm(self):
        print(f"Fire alarm is ringing...")
        for m in self.elevators:
            m.go_to_floor(m.bottom)