class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0]*len(temperatures)
        stack =[]

        for i, temp in enumerate(temperatures):
            while stack and temp > temperatures[stack[-1]]:
                previndex = stack.pop()
                res[previndex] = i-previndex
            stack.append(i) 
        return res    