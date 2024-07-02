from typing import List

from strategies.strategy import Strategy


class OddEvenStrategy(Strategy):

    def get_slot(slots: List):
        odd_slot = "Not Found"
        for i in range(len(slots)):
            if i % 2 != 0 and slots[i].get_vehicle() is None:
                odd_slot = "Found"
                return slots[i].id
        if odd_slot == "Not Found":
            for i in range(len(slots)):
                if i % 2 == 0 and slots[i].get_vehicle() is None:
                    return slots[i].id
        return "Parking Full."



