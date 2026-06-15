# 1 to N using Head Recursion

def print_numbers_1(i, n: int):
    if i > n:
        return
    print(i)
    print_numbers_1(i + 1, n)

# 1 to N using Tail Recursion

def print_numbers_2(i, n:int):
    if i>n:
        return
    print_numbers_2(i, n - 1)
    print(n)

def print_numbers_3(n:int):
    if n == 0:
        return
    print_numbers_3(n - 1)
    print(n)

# N to 1 using Head Recursion
def print_numbers_4(n:int):
    if n == 0:
        return
    print(n)
    print_numbers_4(n - 1)
# N to 1 using Tail Recursion
def print_numbers_5(i:int, n:int):
    if i > n:
        return
    print_numbers_5(i+1, n)
    print(i)
if __name__ == "__main__":
    # print_numbers_1(1, 5)
    # print_numbers_2(1, 5)
    # print_numbers_3(5)
    # print_numbers_4(5)
    print_numbers_5(1, 5)