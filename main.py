from models.car import Car
from models.parking_lots import ParkingLot
from strategies.descending_strategy import DescendingStrategy
from strategies.odd_even_strategy import OddEvenStrategy

pl = ParkingLot(10, strategy=OddEvenStrategy)
pl.create_slots()

car_1 = Car("dl123", "White")
car_2 = Car("dl344", "Black")
car_3 = Car("dl333", "Maroon")
car_4 = Car("dl304", "Black")
pl.park_car(car_1, 11)
pl.park_car(car_2, 2)
pl.park_car(car_3, 4)
pl.park_car(car_4, 4)
print(pl.get_slots_info())
print(pl.leave_car(car_2.get_registration_num(), 4))
print(pl.parking_stats())
print(pl.get_slot_using_reg_num("dl344"))
print(pl.get_slot_using_reg_num("dl123"))
print(pl.get_car_using_slot_id(1))
print(pl.get_car_using_slot_id(3))
print(pl.get_same_color_car_reg_numbers("Black"))

print(pl.get_slot_using_reg_num("dl333"))
print(pl.leave_car(car_1.get_registration_num(), 6))
print(pl.get_same_color_car_slot_ids("Black"))
print(pl.get_same_color_car_slot_ids("Red"))
