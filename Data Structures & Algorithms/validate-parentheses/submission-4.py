class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeopen = {")":"(", "}":"{", "]":"["}
        
        for p in s:
            if p in closeopen:
                if stack and stack[-1] == closeopen[p]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(p)
        return True if not stack else False                    
