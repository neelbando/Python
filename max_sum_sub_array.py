def max_sum_sub_array(lst):
    max_sum = 0
    cur_sum = 0
    for i in lst:
        cur_sum = cur_sum + i
        if cur_sum > max_sum:
            max_sum = cur_sum
            
        if cur_sum < 0:
            cur_sum = 0
    return max_sum

# lst1 = [-5,4,6,-3,4,1]  #output 12
# lst1 = [5,-4,-2,6,-1]     #output 6
lst1 = [-1,-3,5,-4,3,-6,9,2]   #output 11

print(max_sum_sub_array(lst1))

#this is Kadence algo --> O(n)