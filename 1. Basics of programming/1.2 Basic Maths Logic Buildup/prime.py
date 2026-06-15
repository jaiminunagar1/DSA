# 1. BruteForce Approach

def isprime(n:int)-> bool:
    if n <= 1:
        return False
    for i in range (2,n):
        if n % i == 0:
            return False
    return True
    
if __name__ == "__main__":
    num = int(input("Enter a number: "))
    print(isprime(num))