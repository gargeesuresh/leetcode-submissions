def check_palindrome(s,i,j):
    if(s==s[::-1]):
        print("pal")
        return True
    s=s[i:j+1]
    if(s==s[::-1]):
        return True
    return False

class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if(check_palindrome(s,0,len(s))):
            return s
        i=len(s)-1
        while(i>0):
            if (s[i]==s[0] and check_palindrome(s,0,i)):
                return s[i+1:][::-1]+s
            i-=1
        return s[1:][::-1]+s
               
        