class Solution:
    def breakPalindrome(self, s: str) -> str:
        if len(s)==1:
            return ""
        if(s[0]!="a"):
            return "a"+s[1:]
        i=0
        while(s[i]=="a"):
            if(i==len(s)-1):
                return s[:-1]+"b"
            i+=1
        if(len(s)%2==1 and int((len(s)-1)/2)==i):
            return s[:-1]+"b"
        return s[:i]+"a"+s[i+1:]