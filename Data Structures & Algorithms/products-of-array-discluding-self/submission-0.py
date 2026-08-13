class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = []
        right = [0]*len(nums)
        product = 1
        for i in range(len(nums)):
            left.append(product)
            product *= nums[i]
        product=1            
        for i in range(len(nums)-1,-1,-1):
            right[i] = product    
            product *= nums[i]

        return [left[i]*right[i] for i in range(len(nums))]    
            


  


                
            
            
            
            
        