def insertion_sort(lst):
    for i in range(1,len(lst)):
        while i > 0 :
            if lst[i] < lst[i-1]:
                lst[i],lst[i-1]=lst[i-1],lst[i]
            i = i-1
    return lst
    

# lst1 = [1,3,4,2,7,5,6,0]
# lst1 = [2,3,4,1,7,5,6,0]
# print(insertion_sort(lst1))
print(insertion_sort([7,8,9,8,7,6,5,6,7,8,9,8,7,6,5,6,7,8]))