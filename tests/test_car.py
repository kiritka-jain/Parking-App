import unittest

from models.car import Car


class TestCar(unittest.TestCase):
    car_1 = Car("dl123", "White")

    def test_get_registration_num(self):
        self.assertEqual(self.car_1.get_registration_num(), "dl123")

    def test_set_registration_num(self):
        self.car_1.set_registration_num("dl555")
        self.assertEqual(self.car_1.get_registration_num(), "dl555")

    def test_get_color(self):
        self.assertEqual(self.car_1.get_color(), "White")

    def test_set_color(self):
        self.car_1.set_color("Red")
        self.assertEqual(self.car_1.get_color(), "Red")


if __name__ == '__main__':
    unittest.main()
