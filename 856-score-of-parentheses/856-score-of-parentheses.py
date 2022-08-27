from collections import deque
 


 
class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        que = deque()
        score=0
        for i in range(len(s)):
            el=s[i]
            if(el=="("):
                que.append("(")
            elif(el==")" and que[-1]=="(" ):
                que.pop()
                que.append(1)
            elif(el==")"):
                inside=0
                while(que[-1]!="("):
                    inside+=que.pop()
                que.pop()
                que.append(2*inside)
        while(que):
            score+=que.pop()
        return score
                
            