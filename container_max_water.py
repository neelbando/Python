def maxarea(lst):
    left_pointer = 0
    right_pointer = len(lst)-1
    max_area = 0
    
    while left_pointer < right_pointer:
        wirdth = right_pointer - left_pointer
        hight = min(lst[left_pointer],lst[right_pointer])
        area = wirdth * hight
        max_area = max(max_area,area)
        
        if lst[left_pointer] > lst[right_pointer]:
            right_pointer = right_pointer - 1
        else:
            left_pointer = left_pointer + 1
    
    return max_area


lst1 = [1,8,6,2,5,4,8,3,7]  
print(maxarea(lst1))
