class Solution:
    def check(self, piles, h, k):
        t=0
        for pile in piles:
            t+=ceil(pile/k)
            if t>h:
                return False
        return True
    
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        piles.sort()

        left = ceil(sum(piles)/h)
        right = piles[-1]
        
        while(left<right):
            mid = left + int((right - left)/2)

            if self.check(piles, h,mid):
                right = mid 
            else:
                left = mid + 1
        
        return right