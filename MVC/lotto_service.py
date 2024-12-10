import random
from lotto import Lotto


class LottoService:
    @staticmethod
    def auto():
        numbers = random.sample(range(1, 46), 6)
        return Lotto(sorted(numbers))
    @staticmethod
    def manual(numbers):
        return Lotto(sorted(numbers))