def check_palidrome(s:str) -> bool:
    l=0
    r=len(s)-1
    while l<r:
        if s[l] != s[r]:
            return False
        l +=1
        r -=1
    return True
def check_usingrecursion(s:str,l,r)->bool:
    if l>=r:
         return True
    if s[l] != s[r]:
            return False    
    return check_usingrecursion(s,l+1,r-1)
if __name__ == '__main__':
    s = input("Enter string")
    print(check_palidrome(s))
    print(check_usingrecursion(s,l=0,r=len(s)-1))