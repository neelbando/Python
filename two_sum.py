def two_sum(arr, tgt):
    d = {}
    for i,v in enumerate(arr):
        diff = tgt - v
        if diff in d:
            return (d[diff],i)
        else:
            d[v] = i

arr1 = [2,7,11,15,34,8,6]
tgt1 = 19

print(two_sum(arr1, tgt1))
