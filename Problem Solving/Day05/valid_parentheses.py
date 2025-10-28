# Problem Link : https://leetcode.com/problems/valid-parentheses/description/
# Submission Link : https://leetcode.com/problems/valid-parentheses/submissions/1812264316/

def isValid(s: str) -> bool:
    stack = []
    mapping = {')':'(', ']':'[', '}':'{'}
    flag = True
    for par in s:
        if par in "([{":
            stack.append(par)
        else:
            if (mapping[par] not in stack) or (len(stack) != 0 and mapping[par] != stack.pop()):
                flag = False
                break
    if len(stack) != 0:
        flag = False
    return flag