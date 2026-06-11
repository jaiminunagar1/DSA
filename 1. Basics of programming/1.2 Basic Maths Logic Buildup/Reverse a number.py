def reverse_number(num):
    is_negative = False
    if num < 0:
        is_negative = True
    n=abs(num)
    Ans = 0
    while n>0:
        last_digit = n % 10
        Ans = Ans * 10 + last_digit
        n = n // 10
    if Ans < (-(2**31)) or Ans > (2**31 - 1):
            return 0
    if is_negative:
        Ans = -Ans
    return Ans 
    

if __name__ == "__main__":
    num = int(input("Enter a number: "))
    print(reverse_number(num))