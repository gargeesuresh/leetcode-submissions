class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_map={} 
        t_map={} 
        for i in range(len(s)):
            if ((s[i] in s_map and s_map[s[i]]!=t[i]) or (t[i] in t_map and t_map[t[i]]!=s[i])):
                return False
            if (s[i] not in s_map and t[i] not in t_map):
                s_map[s[i]]=t[i] 
                t_map[t[i]]=s[i]
            # if((s[i] in s_map and t[i] not in t_map) or (t[i] in t_map and s[i] not in s_map)):
            #     return False
        return True
                