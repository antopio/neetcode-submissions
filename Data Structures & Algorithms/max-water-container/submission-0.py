class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # distance in between elements is the width?
        # can't sort, order actually matters a lot here
        # brute force: compare each to each. yuck

        # 2 pointer problem
        max_area = 0
        i = 0
        j = len(heights) - 1
        while i<j:
            area = min(heights[i], heights[j]) * (j-i)
            if area > max_area:
                max_area = area
            # move the shorter wall inwards
            if heights[i] > heights[j]:
                j -= 1
            else:
                i += 1
            
        return max_area