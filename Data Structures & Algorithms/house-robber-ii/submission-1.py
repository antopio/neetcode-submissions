class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        elif len(nums) == 1:
            return nums[0]

        # because circle, [0] and [-1] can never be together (they are beside eachother). 
        # either exclude house 0 or house -1. 
        return max(self.street_robber(nums[1:]), self.street_robber(nums[:-1]))

    def street_robber(self, nums):
        rob1 = 0
        rob2 = 0
        for house in nums:
            max_money = max(rob1 + house, rob2)
            rob1 = rob2
            rob2 = max_money

        return max(rob1, rob2)


