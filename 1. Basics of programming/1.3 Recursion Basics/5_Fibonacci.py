# using Simple For loop

def Fib_1(n:int)-> int:
    n1=0
    n2=1
    for _ in range(0,n):
        temp = n2
        n2 = n1+n2
        n1=temp
    return n1

# Using Resursion

def Fib_2(n:int)->int:
    if n == 0 or n==1:
        return n
    return Fib_2(n-1)+Fib_2(n-2)

if __name__ == '__main__':
    n = int(input('Enter any number: '))
    print(Fib_1(n))
    print(Fib_2(n))