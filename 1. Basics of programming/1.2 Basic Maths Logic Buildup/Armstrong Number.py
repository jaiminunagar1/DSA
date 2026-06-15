def isarmstrong(num:int)-> bool:
    n = num
    count = len(str(num))
    sum = 0
    while n > 0:
        ld = n % 10
        sum = sum + (ld ** count)
        n = n // 10
    return sum == num

if __name__ == "__main__":
    num = int(input("Enter a number: "))
    print(isarmstrong(num))