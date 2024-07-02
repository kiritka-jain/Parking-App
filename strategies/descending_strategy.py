from typing import List

from strategies.strategy import Strategy


class DescendingStrategy(Strategy):

    def get_slot(slots: List):
        rev_slots = slots[::-1]
        for slot in rev_slots:
            if slot.get_vehicle() is None:
                return slot.id
        return None
