class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        matching = {}
        for word in strs:
            key = "".join(sorted(word))
            if key in matching:
                matching[key].append(word)
            else:    
                matching[key] = [word]


        return list(matching.values())
            