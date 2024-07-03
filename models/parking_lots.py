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
        self.empty = capacity
        self.occupied = 0
        self.same_color_cars_reg_num = {}

    def get_slots(self):
        return self.slots

    def set_strategy(self, strategy: Strategy):
        self.strategy = strategy

    def park_car(self, car, entry_time):
        available_slot = self._get_free_slot()
        if available_slot is None:
            return "Parking full. No slot available."
        self.slots[available_slot].set_vehicle(car)
        reg_num = car.get_registration_num()
        ticket_id = str(available_slot) + "a"
        new_ticket = Ticket(ticket_id, reg_num, entry_time)
        self.tickets[reg_num] = new_ticket
        self.occupied += 1
        self.empty -= 1
        color = car.get_color()
        reg_num = car.get_registration_num()
        if color not in self.same_color_cars_reg_num:
            self.same_color_cars_reg_num[color] = [reg_num]
        else:
            self.same_color_cars_reg_num[color].append(reg_num)

        return "Car parked successfully."

    def leave_car(self, car_reg_num, exit_time):
        slot = self._get_slot_by_reg_number(car_reg_num)

        if not slot:
            return "Car not found."

        try:
            self.tickets[car_reg_num].set_exit_time(exit_time)

        except InvalidExitTimeException:
            print("Invalid leave time")
            return

        amount = self.tickets[car_reg_num].get_amount_to_pay()
        print("Your parking charges are Rupees:", amount)
        self.empty += 1
        self.occupied -= 1
        car_col = self._get_car_by_reg_num(car_reg_num)
        self.same_color_cars_reg_num[car_col].remove(car_reg_num)
        return slot.empty_slot()

    def create_slots(self):
        for i in range(self.capacity):
            self.slots.append(Slot(i))

    def get_slots_info(self):
        all_slots = {}
        for i in range(self.capacity):
            vehicle = self.slots[i].get_vehicle()
            if vehicle is not None:
                all_slots[i] = (vehicle.get_registration_num())
            else:
                all_slots[i] = vehicle
        return all_slots

    def _get_free_slot(self):
        return self.strategy.get_slot(self.slots)

    def parking_stats(self):
        return "empty:", self.empty, "occupied:", self.occupied

    def get_slot_using_reg_num(self, reg_num):
        slot = self._get_slot_by_reg_number(reg_num)

        if not slot:
            return "Car with given registration number not found."

        return "slot_id:", slot.id

    def get_car_using_slot_id(self, slot_id):
        vehicle = self.slots[slot_id].get_vehicle()

        if not vehicle:
            return "Car not found on given slot."

        return vehicle.get_registration_num()

    def get_same_color_car_reg_numbers(self, color):
        if color not in self.same_color_cars_reg_num:
            return "No car of given color is parked in the parking lot."
        same_color_vehicles = self.same_color_cars_reg_num[color]
        return same_color_vehicles

    def get_same_color_car_slot_ids(self, color):
        if color not in self.same_color_cars_reg_num or not self.same_color_cars_reg_num[color]:
            return "No car of given color is parked in the parking lot."

        slot_id_list = []
        reg_num_list = self.same_color_cars_reg_num[color]

        for reg_num in reg_num_list:
            slot = self._get_slot_by_reg_number(reg_num)
            if slot is not None:
                slot_id_list.append(slot.id)

        return slot_id_list

    def _get_slot_by_reg_number(self, reg_number) -> Slot:
        for i in range(self.capacity):
            vehicle = self.slots[i].get_vehicle()
            if vehicle is not None and vehicle.get_registration_num() == reg_number:
                return self.slots[i]
        return None

    def _get_car_by_reg_num(self, reg_num):
        for i in range(self.capacity):
            vehicle = self.slots[i].get_vehicle()
            if vehicle is not None and vehicle.get_registration_num() == reg_num:
                return vehicle.get_color()
