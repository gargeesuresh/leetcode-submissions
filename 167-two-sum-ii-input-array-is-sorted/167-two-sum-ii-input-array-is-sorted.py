class Solution:
    def twoSum(self, n: List[int], t: int) -> List[int]:
        p1=0
        p2=len(n)-1
        while(p1<p2):
            if(n[p1]+n[p2]==t):
                return([p1+1,p2+1])
            elif(n[p1]+n[p2]<t):
                p1+=1
            else:
                p2-=1
        return([p1+1,p2+1])