class Solution:

    def encode(self, strs: List[str]) -> str:
        result = []
        for word in strs:
            result.append(str(len(word))+"#"+word)

        return "".join(result)   


    def decode(self, s: str) -> List[str]:
        result = []
        marker = "#"
        i = 0
        
        while i < len(s):
            length_end = s.find("#", i)
            length = int(s[i:length_end]) 
            word = s[length_end+1 : length_end+1+length]
            result.append(word)
            i = length_end+1+length

        return result    

            







