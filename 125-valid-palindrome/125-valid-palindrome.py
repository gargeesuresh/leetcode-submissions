class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        i=0
        while(i<len(s)):
            if (s[i].isalnum()):
                i+=1
                pass
            else:
                s=s.replace(s[i],"")    
        # s=s.replace(" ","")
        if(s==s[::-1]):
            return True
        return False
        