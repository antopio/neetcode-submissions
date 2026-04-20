class Solution:
    def isValid(self, s: str) -> bool:
        
        brackets = {
             ')' : '(',
             ']' : '[',
             '}' : '{',
        }
        if s[0] in [']', '}', ')']:
            # auto false if opens with a closing bracket. 
            return False

        stack = []

        for i in s:
            if i not in brackets.keys():
                stack.append(i)
            elif i in brackets.keys():
                if brackets[i] not in stack:
                    return False
                elif stack and brackets[i] == stack[-1]:
                    stack.pop()

        if not stack:
            return True
        else:
            return False
        

