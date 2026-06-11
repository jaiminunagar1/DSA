
# 1.Brute Force Solution


def count_digits(n:int):
    num = abs(n)
    count=0
    while num>0:
        count+=1
        num=num//10
    return count
num = int(input("Enter a number: "))
print(count_digits(num))

# 2.Optimal Solution

from math import log10
def count_digits(n:int):
    num = abs(n)
    if num == 0:
        return 1
    float_number = log10(num) + 1
    return int(float_number)

num = int(input("Enter a number: "))
print(count_digits(num))