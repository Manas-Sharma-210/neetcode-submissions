class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxarea = 0
        stack = []

        for i in range(len(heights)):
            while stack and heights[i] < heights[stack[-1]]:
                pop_index = stack.pop()
                h = heights[pop_index]
                width = i if not stack else i - stack[-1] -1
                area = h*width
                maxarea = max(maxarea, area)
            stack.append(i)
        while stack:
            pop_index = stack.pop()
            h = heights[pop_index]
            width = (len(heights) if not stack else len(heights) - stack[-1] -1)
            maxarea = max(maxarea, h*width)
        return maxarea        


        