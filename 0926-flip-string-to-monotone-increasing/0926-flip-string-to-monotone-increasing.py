class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        ones=0
        flips=0
        for num in s:
            if num=='1':
                ones+=1
            elif ones>0:
                flips+=1
                ones-=1
        return flips