def issorted(arr:list) -> bool:

    for i in range(0,len(arr)-1):
        if arr[i] > arr [i+1]:
            return False
        
    return True

if __name__ == "__main__":

    arr1 = [1,2,3,4,5,6]
    arr2 = [5,4,7,9]

    print(f"result of arr1 : {issorted(arr1)}")
    print(f"result of arr1 : {issorted(arr2)}")