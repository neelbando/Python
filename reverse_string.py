str1 = ['h','e','l','l','o']   #output olleh
def reverse_str(strx):
    l=0
    r = len(strx) - 1
    while l < r:
        strx[l],strx[r] = strx[r],strx[l]
        l = l+1
        r = r-1
    
    return strx

print(reverse_str(str1))

    
