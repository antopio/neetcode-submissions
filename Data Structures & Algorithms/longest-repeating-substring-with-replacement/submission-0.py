class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        left = 0
        maxFreq = 0
        res = 0 # biggest valid window

        for right in range(len(s)):
            count[s[right]] = count.get(s[right], 0) + 1
            maxFreq = max(maxFreq, count[s[right]])

            if (right - left + 1) - maxFreq > k:
                count[s[left]] -= 1
                left += 1
            
            res = max(res, right - left + 1)

        return res
