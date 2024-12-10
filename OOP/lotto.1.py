# 절차지향 프로그래밍_random


# import random
#
# def auto_lotto():
#     numbers = [i for i in range(1,46)]
#     random.shuffle(numbers)
#     return numbers
#
# def main():
#     print(auto_lotto())
#
# if __name__ =='__main__':
#     main()


import random

def generate_lotto_numbers():
    lotto_numbers = set()
    while len(lotto_numbers) < 6:
        number = random.randint(1, 45)
        lotto_numbers.add(number)
    return sorted(lotto_numbers)

# 로또 번호 출력
print(generate_lotto_numbers())
