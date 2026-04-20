class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        k = 1
        max_bananas = max(piles)


        # looking for a range between 2 numbers. 1 and max_bananas
        while k <= max_bananas:
            mid = (k + max_bananas) // 2

            if self.can_finish(mid, piles, h):
                res = mid # best result so far. 
                max_bananas = mid - 1
            else:
                k = mid + 1

        return res
            
    def can_finish(self, k, piles, h):
        total = 0
        for i in piles:
            time = math.ceil(i/k)
            total += time
        
        if total <= h:
            return True
        else:
            return False
            
        

        
        



        