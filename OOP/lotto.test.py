##Test 코드


import unittest
from oop.lotto3 import Lotto

class TestLotto(unittest.TestCase)
    def test_lotto_initialization(self):
        lotto = Lotto([1,2,3,4,5,6])
        self.assertEqual(lotto.numbers, [1,2,3,4,5,6])
        input()
        with self.assertRaises(ValueError) as cm:
            Lotto([1,2,3,4,5,6])
        self.assertEqual(str(cm.exception), '6개의 숫자를 입력해 주세요')

        # Duplicate numbers
        with self.assertRaises(ValueError) as cm:
            Lotto([1,2,3,4,5,5])
            self.assertEqual(str(cm.exception), '중복된 숫자가 있습니다.')

        # Numbers out of range
        with self.assertRaises(ValueError) as cm:
            Lotto([0,1,2,3,4,5,6])
        self.assertEqual(str(cm.exception), '숫자는 1~45 사이여야 합니다.')

        with self.assertRaises(valueError) as cm:
            Lotto([1,2,3,4,5,46])
        self.assertEqual(str(cm.exception), '숫자는 1~45 사이여야 합니다.')

if __name__ =='__main__':
    unittest.main()
#



import unittest
from unittest.mock import patch

class TestLottoGenerator(unittest.TestCase):
    def setUp(self):       ##setUp: 테스트 클래스가 생성될 때마다 LottoGenerator 객체를 초기화
        self.generator = LottoGenerator()

    def test_generate_numbers_length(self):
        numbers = self.generator.generate_numbers()
        self.assertEqual(len(numbers), 6, "생성된 숫자의 개수가 6개가 아닙니다.")

    def test_generate_numbers_uniqueness(self):
        numbers = self.generator.generate_numbers()
        self.assertEqual(len(numbers), len(set(numbers)), "생성된 숫자에 중복이 있습니다.")

    def test_generate_numbers_range(self):
        numbers = self.generator.generate_numbers()
        for number in numbers:
            self.assertTrue(1 <= number <= 45, f"숫자 {number}가 1~45 범위를 벗어났습니다.")

if __name__ == '__main__':
    unittest.main()


