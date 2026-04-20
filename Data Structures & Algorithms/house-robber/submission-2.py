class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1 = 0
        rob2 = 0

        for house in nums:
            max_dollars = max(rob1 + house, rob2)
            rob1 = rob2
            rob2 = max_dollars

        return max(rob1, rob2)