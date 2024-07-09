import unittest

from models.car import Car
from models.parking_lots import ParkingLot
from strategies.ascending_strategy import AscendingStrategy
from strategies.descending_strategy import DescendingStrategy


class TestParkingLot(unittest.TestCase):

    def test_get_slots(self):
        pl = ParkingLot(10)
        pl.create_slots()
        total_slots = pl.get_slots()
        actual_ans = len(total_slots)
        expected_ans = 10
        self.assertEqual(actual_ans, expected_ans)

    def test_set_strategy(self):
        pl = ParkingLot(10)
        default_strategy = AscendingStrategy
        self.assertEqual(pl.strategy, default_strategy)
        new_strategy = DescendingStrategy
        pl.set_strategy(new_strategy)
        self.assertEqual(pl.strategy, new_strategy)

    def test_park_car(self):
        pl = ParkingLot(10)
        pl.create_slots()
        car_1 = Car("dl123", "White")
        out = pl.park_car(car_1, 11)
        expected_out = "Car parked successfully."
        self.assertEqual(out, expected_out)
        self.assertEqual(pl.occupied, 1)
        self.assertEqual(pl.empty, pl.capacity - 1)

    def test_park_car_when_car_already_parked(self):
        pl = ParkingLot(10)
        pl.create_slots()
        car_1 = Car("dl123", "White")
        pl.park_car(car_1, 11)
        car_2 = Car("dl123","White")
        out = pl.park_car(car_2,15)
        expected_out = "Car with this registration number already parked ."
        self.assertEqual(out, expected_out)

    def test_park_car_when_parking_full(self):
        pl = ParkingLot(1)
        pl.create_slots()
        car_1 = Car("dl123", "White")
        out = pl.park_car(car_1, 11)
        expected_out = "Car parked successfully."
        self.assertEqual(out, expected_out)
        car_2 = Car("dl1234", "White")
        out2 = pl.park_car(car_2, 12)
        expected_out = "Parking full. No slot available."
        self.assertEqual(expected_out, out2)

    def test_leave_car(self):
        pl = ParkingLot(10)
        pl.create_slots()
        car_1 = Car("dl123", "White")
        pl.park_car(car_1, 11)
        actual_ans = pl.leave_car(car_1.get_registration_num(), 17)
        expected_ans = "Thanks for your Visit."
        self.assertEqual(actual_ans, expected_ans)
        self.assertEqual(pl.empty, 10)

    def test_leave_car_when_car_not_present(self):
        pl = ParkingLot(10)
        pl.create_slots()
        car_1 = Car("dl123", "White")
        actual_ans = pl.leave_car(car_1.get_registration_num(), 17)
        expected_ans = "Car not found."
        self.assertEqual(actual_ans, expected_ans)

    def test_leave_car_when_exit_time_smaller_than_entry_time(self):
        pl = ParkingLot(10)
        pl.create_slots()
        car_1 = Car("dl123", "White")
        pl.park_car(car_1, 20)
        actual_ans = pl.leave_car(car_1.get_registration_num(), 17)
        expected_ans = None
        self.assertEqual(actual_ans, expected_ans)

    def test_parking_stats(self):
        pl = ParkingLot(10)
        pl.create_slots()
        car_1 = Car("dl123", "White")
        pl.park_car(car_1, 11)
        actual_ans = pl.parking_stats()
        expected_ans = ('empty:', 9, 'occupied:', 1)
        self.assertEqual(actual_ans, expected_ans)

    def test_get_slots_info(self):
        pl = ParkingLot(10)
        pl.create_slots()
        car_1 = Car("dl123", "White")
        pl.park_car(car_1, 11)
        actual_ans = pl.get_slots_info()
        expected_ans = {0: "dl123", 1: None, 2: None, 3: None, 4: None, 5: None, 6: None, 7: None, 8: None, 9: None}
        self.assertEqual(actual_ans, expected_ans)

    def test_get_slot_using_reg_num(self):
        pl = ParkingLot(10)
        pl.create_slots()
        car_1 = Car("dl123", "White")
        pl.park_car(car_1, 11)
        actual_ans = pl.get_slot_using_reg_num("dl123")
        expected_ans = ('slot_id:', 0)
        self.assertEqual(actual_ans, expected_ans)

    def test_get_car_using_slot_id(self):
        pl = ParkingLot(10)
        pl.create_slots()
        car_1 = Car("dl123", "White")
        pl.park_car(car_1, 11)
        actual_ans = pl.get_car_using_slot_id(0)
        expected_ans = "dl123"
        self.assertEqual(actual_ans, expected_ans)

    def test_get_same_color_car_reg_numbers(self):
        pl = ParkingLot(10)
        pl.create_slots()
        car_1 = Car("dl123", "White")
        pl.park_car(car_1, 11)
        actual_ans = pl.get_same_color_car_reg_numbers("White")
        expected_ans = ["dl123"]
        self.assertEqual(actual_ans, expected_ans)

    def test_get_same_color_car_slot_ids(self):
        pl = ParkingLot(10)
        pl.create_slots()
        car_1 = Car("dl123", "White")
        pl.park_car(car_1, 11)
        actual_ans = pl.get_same_color_car_slot_ids("White")
        expected_ans = [0]
        self.assertEqual(actual_ans, expected_ans)


if __name__ == '__main__':
    unittest.main()
