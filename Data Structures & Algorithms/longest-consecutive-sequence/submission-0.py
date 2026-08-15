class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        myset = set(nums)
        res = 0
        for num in myset:
            if (num-1) not in myset:
                currentnum = num
                currentstreak = 1
                while (currentnum + 1) in myset:
                    currentnum += 1
                    currentstreak +=1
                res = max(res, currentstreak)
        return res            

            
