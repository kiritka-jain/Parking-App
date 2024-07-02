from exceptions.invalid_exit_time_exception import InvalidExitTimeException
from models.slot import Slot
from models.ticket import Ticket
from strategies.ascending_strategy import AscendingStrategy
from strategies.strategy import Strategy


class ParkingLot:
    def __init__(self, capacity: int, strategy=AscendingStrategy):
        self.capacity = capacity
        self.slots = []
        self.strategy = strategy
        self.tickets = {}

    def get_slots(self):
        return self.slots

    def set_strategy(self, strategy: Strategy):
        self.strategy = strategy

    def park_car(self, car, entry_time):
        available_slot = self._get_free_slot()
        if available_slot is None:
            return "Parking full. No slot available."

        self.slots[available_slot].set_vehicle(car)
        ticket_id = str(available_slot) + "a"
        self.tickets[car.get_registration_num()] = Ticket(ticket_id, car.get_registration_num, entry_time)
        return "Car parked successfully."

    def leave_car(self, car_reg_num, exit_time):
        for i in range(self.capacity):
            vehicle = self.slots[i].get_vehicle()
            if vehicle is not None and vehicle.get_registration_num() == car_reg_num:
                try:
                    self.tickets[car_reg_num].set_exit_time(exit_time)
                except InvalidExitTimeException:
                    print("Invalid leave time")
                    return
                amount = self.tickets[car_reg_num].get_amount_to_pay()
                print("Your parking charges are Rupees:", amount)
                return self.slots[i].empty_slot()
        return "Car not found."

    def create_slots(self):
        for i in range(self.capacity):
            self.slots.append(Slot(i))

    def get_slots_info(self):
        all_slots = {}
        for i in range(self.capacity):
            if self.slots[i].get_vehicle() is not None:
                all_slots[i] = (self.slots[i].get_vehicle().get_registration_num())
            else:
                all_slots[i] = (self.slots[i].get_vehicle())
        return all_slots

    def _get_free_slot(self):
        return self.strategy.get_slot(self.slots)

    def parking_stats(self):
        empty = 0
        occupied = 0
        for i in range(self.capacity):
            if self.slots[i].get_vehicle() is None:
                empty += 1
            else:
                occupied += 1
        return "empty:", empty, "occupied:", occupied

    def get_slot_using_reg_num(self, reg_num):
        for i in range(self.capacity):
            slot = self.slots[i].get_vehicle()
            if slot is not None and slot.get_registration_num() == reg_num:
                return "slot_id:", i
        return "Car with given registration number not found."

    def get_car_using_slot_id(self, slot_id):
        slot = self.slots[slot_id].get_vehicle()
        if slot is not None:
            return slot.get_registration_num()
        return "Car not found on given slot."

    def get_same_color_car_reg_numbers(self, color):
        same_color_cars = []
        for i in range(self.capacity):
            if self.slots[i].get_vehicle() is not None and self.slots[i].get_vehicle().get_color() == color:
                same_color_cars.append(self.slots[i].get_vehicle().get_registration_num())
        if not same_color_cars:
            return "No car of given color is parked in the parking lot."
        return same_color_cars

    def get_same_color_car_slot_ids(self, color):
        same_color_car_slots = []
        for i in range(self.capacity):
            if self.slots[i].get_vehicle() is not None and self.slots[i].get_vehicle().get_color() == color:
                same_color_car_slots.append(i)
        if not same_color_car_slots:
            return "No car of given color is parked in the parking lot."
        return same_color_car_slots
