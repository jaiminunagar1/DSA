def is_palindrome(x:int)-> bool:
    if x<0:
        return False
    palindrome = 0
    n = x
    while n > 0:
        last_digit = n % 10
        palindrome = palindrome * 10+ last_digit
        n = n// 10
    return palindrome == x


if __name__ == "__main__":
    num = int(input("Enter a number: "))
    print(is_palindrome(num))