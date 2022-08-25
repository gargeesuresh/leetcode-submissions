class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if(len(s)!=len(goal)):
            return False
        i1=-1
        i2=-1
        count=0
        charset=set()
        for i in range (len(s)):
            charset.add(s[i])
            if s[i]!=goal[i]:
                count+=1
                if(i1==-1):
                    i1=i
                if(i1!=-1):
                    i2=i
        
        if(count==0 and len(charset)<len(s)):
            return True
        elif(count!=2):
            return False
        else:
            if(s[i1]!=goal[i2] or s[i2]!=goal[i1]):
                return False
        return True
        
                