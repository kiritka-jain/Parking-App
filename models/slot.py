from models.car import Car


class Slot:
    def __init__(self, _id):
        self.id = _id
        self.vehicle = None

    def set_vehicle(self, car: Car):
        self.vehicle = car

    def get_vehicle(self):
        return self.vehicle

    def empty_slot(self):
        self.vehicle = None
