def longest_valid_parenthesis(str):
    open_braket_count = 0     
    close_braket_count = 0 
    max_len = 0
    
    for i in str:
        if i == '(':
            open_braket_count = open_braket_count + 1
        if i == ')':
            close_braket_count = close_braket_count + 1   
            
        
        if open_braket_count == close_braket_count:
            length = open_braket_count * 2
            max_len = max(max_len,length)
        
        if open_braket_count < close_braket_count:
            open_braket_count = 0
            close_braket_count = 0
            
    return max_len
    
strx = '())(())(((())))'
print(longest_valid_parenthesis(strx))






#******************************************************************************
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
    
    
