def merge_sort(arr):
    print(arr)
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left_arr = arr[:mid]
    rigt_arr = arr[mid:]
    
    left_arr = merge_sort(left_arr)
    rigt_arr = merge_sort(rigt_arr)
    
    print(f"left_arr: {left_arr}")
    print(f"rigt_arr: {rigt_arr}")

    return merge_sorted_array(left_arr,rigt_arr)


def merge_sorted_array(a,b):
    final_arr = []
    i=j=0
    while i < len(a) and j < len(b):
        if a[i] > b[j]:
            final_arr.append(b[j])
            j = j+1
        else:
            final_arr.append(a[i])
            i = i+1  
            
    if i != len(a):
        for itm in range(i,len(a)):
            final_arr.append(a[itm])
            
    if j != len(b):
        for itm in range(j,len(b)):
            final_arr.append(b[itm])
            
    return final_arr
    
    
lst = [10, 3, 15, 7, 8, 23, 98, 29]
print(merge_sort(lst))
# a1 = [17,21,29,38]
# b1= [4,9,25,32,40,42,60,75]

# print(merge_sorted_array(a1,b1))
            
            
            
    