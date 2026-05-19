import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high = 1, max(piles)

        while low < high:
            k = (low + high) // 2  # mid-point candidate speed
            
            hrs = sum(math.ceil(pile / k) for pile in piles)
            
            if hrs <= h:
                high = k       # k might be the answer, but try slower
            else:
                low = k + 1    # too slow, must go faster
        
        return low  # low == high, the minimum valid speed