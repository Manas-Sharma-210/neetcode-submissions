class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 1
        maxprofit = 0
        while right < len(prices):
            if prices[left] < prices[right]:
                currentprofit = prices[right] - prices[left]
                maxprofit = max(currentprofit, maxprofit)
            else:
                left = right
            right += 1    
        return maxprofit            