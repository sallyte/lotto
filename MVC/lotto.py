def validate(numbers):
    if len(numbers) != 6:
        raise ValueError('6개의 숫자를 입력해주세요.')
    if len(set(numbers)) != 6:
        raise ValueError('중복된 숫자가 있습니다.')
    if any(number < 1 or number > 45 for number in numbers):
        raise ValueError('숫자는 1~45 사이여야 합니다')

class Lotto:
    def __init__(self, numbers):
        validate(numbers)
        self.numbers = numbers

    def draw(self):
        return self.numbers

    def __str__(self):
        return str(self.numbers)