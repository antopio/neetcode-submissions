class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        # a + b + c = 0
        # b + c = -a
        triplets = [] # initialize our output list
        
        # each unique value of nums will be the "anchor" or "target", and we do 2 sum on the remaining. 
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue # skip the rest if its the same number. we already have triplets for this "anchor". 

            left = i + 1 # we never look left, because we used it as anchor already
            right = len(nums) - 1 # last item of nums. 

            while left < right: # do 2 sum
                total = nums[i] + nums[left] + nums[right]
                if total == 0:
                    triplets.append([nums[i], nums[left], nums[right]])
                    # move both
                    left = left + 1
                    right = right - 1
                    while left < right and nums[left] == nums[left-1]: left += 1
                    while left < right and nums[right] == nums[right+1]: right -= 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1
                    # check if we are sitting on a duplicate, move again if we are:
                

        return triplets 


            
