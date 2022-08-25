class Solution:
    def breakPalindrome(self, s: str) -> str:
        if len(s)==1:
            return ""
        if(s[0]!="a"):
            return "a"+s[1:]
        i=0
        while(i<len(s) and s[i]=="a"):
            i+=1
        if(i==len(s)):
            return s[:-1]+"b"
        if(len(s)%2==1 and int((len(s)-1)/2)==i):
            return s[:-1]+"b"
        return s[:i]+"a"+s[i+1:]