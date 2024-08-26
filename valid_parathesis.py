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
