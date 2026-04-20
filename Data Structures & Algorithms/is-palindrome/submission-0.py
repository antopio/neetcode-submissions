class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered = s.lower()
        filtered = [c for c in filtered if c.isalnum()]
        return filtered == filtered[::-1]