def selection_sort(lst):
    indexing_length = len(lst)-1
    
    for i in range(0,indexing_length):
        min_val = i
        for j in range(i+1,len(lst)):
            if lst[j] < lst[min_val]:
                min_val = j
        if i != min_val:
            lst[min_val],lst[i], = lst[i], lst[min_val]
    return lst

lst1 = [1,3,4,2,7,5,6,0]
print(selection_sort(lst1))


## this is better than bubble sort as its taking less iteration
