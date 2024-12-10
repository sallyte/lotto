from lotto_draw_type import LottoDrawType

class LottoController:
    def __init__(self, service):
        self.service = service

    def run(self, input_type, numbers=None):
        print(self.draw(input_type, numbers))

    def draw(self, input_type, numbers=None):
        if input_type == LottoDrawType.AUTO:
            return self.service.auto()
        elif input_type == LottoDrawType.MANUAL:
            return self.service.manual(numbers)
        else:
            raise ValueError('지원하지 않는 입력 방식입니다.')