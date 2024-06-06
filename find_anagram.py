def find_anagram(s,p):
    if len(s) < len(p): return []
    
    scount, pcount = {}, {}
    
    for i in range(len(p)):
        pcount[p[i]] = 1 + pcount.get(p[i],0)
        scount[s[i]] = 1 + scount.get(s[i],0)
        
    res=[0] if pcount == scount else []
    l=0
    for j in range(len(p),len(s)):
        scount[s[j]] = 1 + scount.get(s[j],0)
        scount[s[l]] = scount[s[l]] - 1
        
        if scount[s[l]] == 0:
            scount.pop(s[l])
            
        l = l+1
        
        if pcount == scount:
           res.append(l) 
    return res
        
s1 = 'cbaebabacdbac'
p1 = 'abc'
print(find_anagram(s1,p1))

    