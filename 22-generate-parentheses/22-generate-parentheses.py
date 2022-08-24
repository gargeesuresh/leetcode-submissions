def gen(n,o,c,s,ans):
    if (o==n and c==n):
        ans.append(s)
    if (o<n):
        gen(n,o+1,c,s+"(",ans)
    if (c<o):
        gen(n,o,c+1,s+")",ans)
    return ans

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans=[]
        return gen(n,0,0,"",ans)
        