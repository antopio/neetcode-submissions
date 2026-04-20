class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chain = []
        max_length = 0
        for i in range(len(list(s))):
            if s[i] in chain:
                limit = chain.index(s[i])
                chain = chain[limit+1:]
                chain.append(s[i])
            else:
                chain.append(s[i])
                max_length = max(len(chain), max_length)

        return max_length