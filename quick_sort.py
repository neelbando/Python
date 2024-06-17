def quick_sort(lst):
    left_arr = []
    right_arr = []
    
    if len(lst) == 0:
        return []
        
    pivot_point = lst.pop()
    
    for i in lst:
        if i > pivot_point:
            right_arr.append(i)
        else:
            left_arr.append(i)
    return quick_sort(left_arr) + [pivot_point] + quick_sort(right_arr)
            

# lst1 = [1,3,4,2,7,5,6,0]
lst1 = [2,3,4,1,7,5,6,0]
print(quick_sort(lst1))
# print(quick_sort([7,8,9,8,7,6,5,6,7,8,9,8,7,6,5,6,7,8]))