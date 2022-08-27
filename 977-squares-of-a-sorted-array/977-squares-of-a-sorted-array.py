class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        if(nums[0]>=0):
            return [pow(x,2) for x in nums]
        p1=0
        p2=0
        while(p2<len(nums) and nums[p2]<0):
            p2+=1
        ans=[]
        p1=p2-1
        marker=p2
        while(p1>=0 and p2<len(nums)):
            if(pow(nums[p1],2)<=pow(nums[p2],2)):
                ans.append(pow(nums[p1],2))
                p1-=1
            else:
                ans.append(pow(nums[p2],2))
                p2+=1
        while(p1>=0):
            ans.append(pow(nums[p1],2))
            p1-=1
        while(p2<len(nums)):
            ans.append(pow(nums[p2],2))
            p2+=1
        return ans