class Solution:
    def generate(self, n: int) -> List[List[int]]:
        ans =[]
        if ans==0:
            return ans
        
        ans.append([1])
        if n ==1:
            return ans
        
        ans.append([1,1])
        if n ==2:
            return ans
        
        for i in range(2,n):
            row=[]
            row.append(1)
            for j in range(i-1):
                row.append(ans[-1][j]+ans[-1][j+1])
            row.append(1)
            ans.append(row)
        return ans