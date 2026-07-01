def merge_array(left:list,right:list) ->list:
    """
    The function is take two sorted array and merge it in to the one sort array.
    """
    result = []
    i,j=0,0
    n,m = len(left),len(right)
    while i<n and j < m:
        if left[i] <= right [j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    if i<n:
        while i<n:
            result.append(left[i])
            i+=1
    if j<m:
        while j<m:
            result.append(right[j])
            j+=1
    return result


def merge_sort(arr:list)->list:
    if len(arr) <= 1:
        return arr
    mid = len(arr)//2
    left_arr = arr[:mid]
    right_arr = arr[mid:]
    left = merge_sort(left_arr)
    right = merge_sort(right_arr)
    return merge_array(left,right)   
    
if __name__ == '__main__':
    # left = [1,2,3,4]
    # right = [1,1,3,4,5,6,7]
    arr = [8, 3, 5, 4, 7, 6, 1, 2]

    # sorted_array = merge_array(left.copy(),right.copy())
    sorted_array = merge_sort(arr)
    print(sorted_array)
    

