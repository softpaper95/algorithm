import math
x = int(input("정수를 입력하세요:"))
def is_prime_number(x):
    for i in range(2, int(math.sqrt(x)) +1):
        if x % i == 0:
            print(False)
            break
        else: print(True)


is_prime_number(x)