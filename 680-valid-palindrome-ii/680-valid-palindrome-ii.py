def check_pal(s):
    if(s==s[::-1]):
        return True
    return False
class Solution:
    def validPalindrome(self, s: str) -> bool:
        l=0
        r=len(s)-1
        count=0
        while(l<r):
            if(s[l]==s[r]):
                l+=1
                r-=1
                continue
            if(check_pal(s[l:r]) or check_pal(s[l+1:r+1])):
               return True
            return False
        return True
            
            
        