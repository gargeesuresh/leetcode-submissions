def pal(s):
    if(s==s[::-1]):
        return True
    return False

class Solution:
    def checkPalindromeFormation(self, a: str, b: str) -> bool:
        if(len(a)==1):
            return True
        length=len(a)
        i=0
        while(i<length and a[i]==b[length-i-1]):
            i+=1
        if(pal(a[i:length-i])):
            return True
        elif(pal(b[i:length-i])):
            return True
        i=0
        while(b[i]==a[length-i-1]):
            i+=1
        if(pal(a[i:length-i])):
            return True
        elif(pal(b[i:length-i])):
            return True
        else:
            return False
        
            