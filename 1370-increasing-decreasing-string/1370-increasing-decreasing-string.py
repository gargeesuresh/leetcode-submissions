class Solution:
    def sortString(self, s: str) -> str:
        mapp ={}
        for i in range(len(s)):
            if(int(ord(s[i])-97) in mapp):
                mapp[int(ord(s[i])-97)]+=1
            else:
                mapp[int(ord(s[i])-97)]=1
        s=""
        while(len(mapp)>0):
            for i in range(0,26):
                if(i in mapp):
                    if(mapp[i]==1):
                        mapp.pop(i)
                    else:
                        mapp[i]-=1
                    s=s+str(chr(i+97))
            for i in range(25,-1,-1):
                if(i in mapp):
                    if(mapp[i]==1):
                        mapp.pop(i)
                    else:
                        mapp[i]-=1
                    s=s+str(chr(i+97))
        return s
