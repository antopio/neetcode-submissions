class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        num_set = set(nums)
        if len(num_set) < len(nums):
            return True
        else:
            return False