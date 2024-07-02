from exceptions.invalid_exit_time_exception import InvalidExitTimeException


class Ticket:
    def __init__(self, id: str, car_reg_num: str, entry_time: int):
        self.id = id
        self.car_reg_num = car_reg_num
        self.entry_time = entry_time
        self.exit_time = 0

    def get_entry_time(self):
        return self.entry_time

    def set_exit_time(self, exit_time):
        if exit_time < self.entry_time:
            raise InvalidExitTimeException

    def get_total_hrs(self):
        time = self.exit_time - self.entry_time
        if time == 0:
            return 1
        return time

    def get_amount_to_pay(self):
        total_time = self.get_total_hrs()
        if total_time <= 3:
            return 50 * total_time
        else:
            return 50 * 3 + (total_time - 3) * 50
