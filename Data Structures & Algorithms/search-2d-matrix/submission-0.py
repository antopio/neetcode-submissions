class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        print(target)
        print(len(matrix))

        # find r:
        for i in range(0, len(matrix)):
            if target <= matrix[i][-1]:

                l = 0
                r = len(matrix[i])-1
                while l <= r:
                    mid = (l+r)//2
                    if target == matrix[i][mid]:
                        return True

                    elif target > matrix[i][mid]:
                        l = mid+1
                    
                    elif target < matrix[i][mid]:
                        r = mid-1
        
        return False
                