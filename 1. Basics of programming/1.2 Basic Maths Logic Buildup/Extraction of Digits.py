
def extractiondigit(num:int):

    n=num    
    while n>0:
        last_digit = n % 10
        print(f"last_digit: {last_digit}")
        n = n // 10
    print(num)

num = int(input("Enter a number: "))
extractiondigit(num)