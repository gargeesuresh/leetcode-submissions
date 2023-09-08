class Solution:
    def trap(self, height: List[int]) -> int:
        l=0
        r=len(height)-1
        lmax=0
        rmax=0
        water=0
        
        while(l<=r):
            rmax,lmax=max(rmax,height[r]),max(lmax,height[l])
            if lmax<rmax:
                water+=lmax-height[l]
                l+=1
            else:
                water+=rmax-height[r]
                r-=1
        return water