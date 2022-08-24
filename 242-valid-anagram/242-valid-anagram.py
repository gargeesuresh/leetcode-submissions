class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s)!=len(t)):
            return False
        s_map={}
        t_map={}
        for i in range(len(s)):
            if(s[i] not in s_map):
                s_map[s[i]]=1
            else:
                s_map[s[i]]+=1
            if(t[i] not in t_map):
                t_map[t[i]]=1
            else:
                t_map[t[i]]+=1
        for element in s_map:
            if( (element not in t_map) or( t_map[element]!=s_map[element])):
                return False
        return True
            