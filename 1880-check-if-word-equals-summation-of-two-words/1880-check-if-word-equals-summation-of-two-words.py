def trim(s):
    i=0
    while(i<len(s) and s[i]=="a" ):
        i+=1
    return s[i:]

def val(s):
    val=0
    if len(s)==0:
        return 0
    for i in range(len(s)):
        val=10*val+int(ord(s[i])-ord('a'))
    return val

class Solution:
    def isSumEqual(self, f: str, s: str, t: str) -> bool:
        f=trim(f)
        s=trim(s)
        t=trim(t)
        f_val=val(f)
        s_val=val(s)
        t_val=val(t)
        if(f_val+s_val==t_val):
            return True
        return False
        