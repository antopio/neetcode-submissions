class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_keys = {}
        for string in strs:
            sorted_word = "".join(sorted(string))
            if sorted_word in sorted_keys:
                sorted_keys[sorted_word].append(string)
            else:
                sorted_keys[sorted_word] = [string]
        
        return list(sorted_keys.values())
        
