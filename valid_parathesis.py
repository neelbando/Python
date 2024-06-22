# def check_valid_parenthesis(strx):
#     stk = []
#     cant_start_with = [")","}","]"]

#     xx = {
#         "(": ")", 
#         ")": "(" ,
#         "{": "}", 
#         "}": "{" ,
#         "[": "]", 
#         "]": "[" 
#         }

#     for v in strx:
#         if not stk:
#             if v in cant_start_with:
#                 return False
#             stk.append(v)
#         else:
#             if v == xx[stk[-1]]:
#                 stk.pop()
#             else:
#                 if v in cant_start_with:
#                     return False
#                 stk.append(v)
            
#     if len(stk) > 0:
#         return False
  
#     return True

def check_valid_parenthesis(s: str) -> bool:
    stack = []
    mapping = {")":"(", "}":"{", "]":"["}

    for char in s:
        if char in mapping.values():
            stack.append(char)
        elif char in mapping.keys():
            if not stack or mapping[char] != stack.pop():
                return False
    
    return not stack

strx1 = "(}{)[{()}]{}"
check_valid_parenthesis(strx1)
