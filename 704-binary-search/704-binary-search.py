
        
class Solution:
    def search(self, nums: List[int], t: int) -> int:
        l=0
        r=len(nums)
        p=l+int((r-l)/2)
        while(p>=0 and p<len(nums) and l<=r):
            if(nums[p]==t):
                return p
            elif(nums[p]>t):
                r=p-1
            else:
                l=p+1
            p=l+int((r-l)/2)
        return -1