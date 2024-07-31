#two sum 2 - (consider starting index as 1)

def two_sum2(arr, tgt):
    l=0
    r=len(arr)-1
    
    while l<r:
        if arr[r] + arr[l] == tgt:
            return [l+1,r+1]
        elif arr[r] + arr[l] > tgt:
            r = r-1
        elif arr[r] + arr[l] < tgt:
            l = l+1
    return[]
 
 arr1 = [1,3,4,5,7,11]   #output [3, 4]
tgt1 = 9   

print(two_sum2(arr1, tgt1))
