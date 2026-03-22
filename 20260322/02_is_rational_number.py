import math


def isRationalNumber(number):
    root = math.isqrt(number)
    return root * root == number


# テスト
print(isRationalNumber(1))    # True
print(isRationalNumber(2))    # False
print(isRationalNumber(3))    # False
print(isRationalNumber(4))    # True
print(isRationalNumber(5))    # False
print(isRationalNumber(9))    # True
print(isRationalNumber(16))   # True
print(isRationalNumber(49))   # True
print(isRationalNumber(225))  # True
