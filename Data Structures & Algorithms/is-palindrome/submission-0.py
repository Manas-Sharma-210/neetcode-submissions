class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleanedtext = "".join(c.lower() for c in s if c.isalnum())
        left = 0
        right = len(cleanedtext)-1
        
        while left < right:
            if cleanedtext[left] == cleanedtext[right]:
                left += 1
                right -= 1
            else:
                return False
        return True            