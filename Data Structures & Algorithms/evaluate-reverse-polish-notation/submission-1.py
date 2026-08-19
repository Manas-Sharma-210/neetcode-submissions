class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {"+", "-", "*", "/"}

        for o in tokens:
            if o not in operators:
                stack.append(int(o))
            else:
                right = stack.pop()
                left = stack.pop()
                if o == "+":
                    result = left+right
                elif o == "-":
                    result = left-right
                elif o =="*":
                    result = left*right
                elif o == "/":
                    result = int(left/right)
                stack.append(result)        
        return stack[0]