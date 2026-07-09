def duplicate(arr:list):
    frequency_map = {}

    for i in range(0,len(arr)):
        frequency_map[arr[i]] = 0

    j = 0

    for k in frequency_map:
        arr[j] = k
        j+=1

    return j

# Optmial

def duplicate(arr:list):
    n = len(arr)
    if n == 1:
        return 1
    # i = 0
    # for j in range(1,n):
    #     if arr[i] != arr[j]:
    #         i+=1
    #         arr[i],arr[j] = arr[j],arr[i]

    i = 0
    j = 1
    while j<n:
        if arr[i] != arr[j]:
            i+=1
            arr[i],arr[j] = arr[j],arr[i]
        j+=1
    return i+1