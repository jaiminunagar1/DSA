# 1.Sum of first N natural numbers without Loop

def sum_n(n:int):
    if n <= 0:
        raise ValueError("n must be a positive integer")
    if n == 1:
        return 1
    return n+sum_n(n-1)


# 2.Fact of N Number

# 2.1 Fact using the for loop

def Fact1(n:int):
    if n == 1 or n == 0:
        return 1
    fact =  1
    for i in range(1,n+1):
        fact =  fact * i
    return fact

# 2.2 Fact using the recursion
def Fact_n(num:int):
    if num == 1 or num == 0:
        return 1
    return num * Fact_n(num-1)

if __name__ == '__main__':
    try:
        n = int(input("Enter the n:"))
        # ans = sum_n(n)
        # ans = Fact_n(n)
        ans = Fact1(n)
        print(ans)
    except ValueError as e:
        print(f"Error:{e}")