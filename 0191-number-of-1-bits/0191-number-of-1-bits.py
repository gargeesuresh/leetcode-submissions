class Solution:
    def hammingWeight(self, n: int) -> int:
        ans=0
        while(n>0):
            ans+=int(n%2)
            n=int(n/2)
        return ans