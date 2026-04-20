class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        for i in range(len(nums)):
            x = nums[:i] + nums[i+1:]
            y = math.prod(x)
            output.append(y)
        
        return output
