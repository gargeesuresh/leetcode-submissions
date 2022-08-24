from queue import LifoQueue


class Solution:
    def isValid(self, s: str) -> bool:
        stack = LifoQueue()
        for i in range(len(s)):
            if(s[i]=="(" or s[i]=="{" or s[i]=="["):
                stack.put(s[i])
            elif(s[i]==")"and (stack.empty() or stack.get()!="(")):
                return False
            elif(s[i]=="}"and (stack.empty() or stack.get()!="{")):
                return False
            elif(s[i]=="]"and (stack.empty() or stack.get()!="[")):
                return False
        if(stack.empty()):
            return True
        else:
            return False