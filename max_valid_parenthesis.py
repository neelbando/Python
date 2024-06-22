strx = '()()()()()(()()()()(()()()()()()()'
stk = []

xx = {"(": ")", ")": "(" }

for i, v in enumerate(strx):
    if not stk:
        stk.append([i,v])
    else:
        if v == xx[stk[-1][1]]:
            stk.pop()
        else:
            stk.append([i,v])
            
stk1 = [i[0] for i in stk]
print(stk1)

maxl = 0
curr = 0
for i in range(len(strx)):
    if i in stk1:
        curr = 0
    else:
        curr = curr+1
        maxl = max(maxl,curr)
print(maxl)
    
    