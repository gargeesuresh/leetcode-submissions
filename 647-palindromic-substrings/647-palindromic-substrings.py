def check_pal(s):
    if(s==s[::-1]):
        return True
    return False
class Solution:
    def countSubstrings(self, s: str) -> int:
        count=0
        for length in range(len(s),0,-1):
            for i in range(0,len(s)-length+1):
                if check_pal(s[i:i+length]):
                    count+=1
        return count