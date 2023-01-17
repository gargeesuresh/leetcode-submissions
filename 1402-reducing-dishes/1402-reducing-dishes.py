class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort(reverse=True)
        sum=0
        ans=0
        for i in satisfaction:
            if i+sum>=0:
                sum+=i
                ans+=sum
            else:
                break
        return ans
            
        