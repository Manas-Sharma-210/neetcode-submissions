class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numfreq = {}
        swappp = []
        

        for num in nums:
            numfreq[num] = numfreq.get(num, 0)+1

        for key, value in numfreq.items():
            swappp.append((value, key))

        swappp = sorted(swappp, reverse=True)

        return [item[1] for item in swappp[:k]]


            
               
                    

            
            