class Car:
    def __init__(self, registration_num: str, color: str):
        self.registration_num = registration_num
        self.color = color

    def get_registration_num(self):
        return self.registration_num

    def set_registration_num(self, num):
        self.registration_num = num

    def get_color(self):
        return self.color

    def set_color(self,color):
        self.color = color




