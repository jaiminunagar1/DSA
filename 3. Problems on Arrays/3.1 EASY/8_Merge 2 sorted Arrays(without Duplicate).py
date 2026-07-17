def mergeduplicate(nums1:list,nums2:list) -> list:
    n,m=len(nums1),len(nums2)
    i,j=0,0
    result = []
    while i<n and j<m:
        if nums1[i]<=nums2[j]:
            if len(result) == 0 or result[-1]!=nums1[i]:
                result.append(nums1[i])
            i+=1
        else:
            if len(result)==0 or result[-1] != nums2[j]:
                result.append(nums2[j])
            j+=1
    while i<n:
        if len(result) == 0 or result[-1]!=nums1[i]:
            result.append(nums1[i])
        i+=1
    while j<m:
        if len(result)==0 or result[-1] != nums2[j]:
                result.append(nums2[j])
        j+=1
    return result
