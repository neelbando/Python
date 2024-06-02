def bubble_sort(lst):
    sorted = False
    while not sorted:
        sorted = True
        for i in range(len(lst)-1):
            if lst[i] > lst[i+1]:
                sorted = False
                lst[i] , lst[i+1] = lst[i+1], lst[i]
    return lst

lst1 = [1,3,2,5,9,7,8,5,4,0]
print(bubble_sort(lst1))






    
