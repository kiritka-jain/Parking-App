from typing import List

from strategies.strategy import Strategy


class AscendingStrategy(Strategy):

    def get_slot(slots: List):
        for slot in slots:
            if slot.get_vehicle() is None:
                return slot.id
        return None
