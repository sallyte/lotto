  ##검증하는 코드


# def validate(numbers):
#     if len(numbers) ! =6:
#         raise ValueError('6개의 숫자를 입력해 주세요.')
#     if len(set(numbers)) ! = 6:
#         raise ValueError('중복된 숫자가 있습니다.')
#     if any(number < 1 or number > 45 for number in numbers):
#         raise ValueError('숫자는 1~45 사이어야 합니다. ')
#
# class Lotto:
#     def __init__(self, numbers):
#         validate(numbers)
#         self.numbers = numbers
#     def draw(self):
#         return self.numbers
#     def __str__(self):
#         return str(self.numbers)


  import random

  class LottoGenerator:
      def __init__(self):
          self.lotto_numbers = set()

      def generate_numbers(self):
          while len(self.lotto_numbers) < 6:
              number = random.randint(1, 45)
              self.lotto_numbers.add(number)
          return sorted(self.lotto_numbers)


  class LottoValidator:
      def __init__(self, numbers):
          self.numbers = numbers

      def validate(self):
          if not self._validate_length():
              return False, "숫자의 개수가 6개가 아닙니다."
          if not self._validate_uniqueness():
              return False, "중복되는 숫자가 있습니다."
          if not self._validate_range():
              return False, "1에서 45 사이의 숫자가 아닙니다."
          return True, "유효한 로또 번호입니다."

      def _validate_length(self):
          return len(self.numbers) == 6

      def _validate_uniqueness(self):
          return len(self.numbers) == len(set(self.numbers))

      def _validate_range(self):
          return all(1 <= number <= 45 for number in self.numbers)


  # 예제 사용
  generator = LottoGenerator()
  lotto_numbers = generator.generate_numbers()
  print(f"생성된 로또 번호: {lotto_numbers}")

  validator = LottoValidator(lotto_numbers)
  is_valid, message = validator.validate()
  print(message)
