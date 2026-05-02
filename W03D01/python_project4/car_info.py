from vehicle_info import Vehicle


class Car(Vehicle):
    def __init__(self, no_of_seatbelt, steering_mode, name, model):
        super().__init__(name, model)
        self.no_of_seatbelt = no_of_seatbelt
        self.steering_mode = steering_mode

    def accelerate(self, acc_pwr):
        self._speed += acc_pwr * 10

    def brake(self, brake_pwr):
        self._speed -= brake_pwr * 20

    def get_speed(self):
        # method overriding is an example of polymorphism
        return f"Speed is {self._speed}"


my_office_car = Car(4, 'Auto', 'My Office Car', 'Tata Nexon')

my_office_car.accelerate(2)

print(my_office_car.get_speed())

my_unknown_testing_vehicle = Vehicle('Tata', 'EV Infinity 3.2')

print(my_unknown_testing_vehicle.get_speed())
