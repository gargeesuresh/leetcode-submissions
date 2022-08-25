# def swap(s,goal):
#     if(len(s)!=len(goal)):
#         return False
#     i1=-1
#     i2=-1
#     count=0
#     charset=set()
#     for i in range (len(s)):
#         charset.add(s[i])
#         if s[i]!=goal[i]:
#             count+=1
#             if(i1==-1):
#                 i1=i
#             if(i1!=-1):
#                 i2=i

#     if(count==0 and len(charset)<len(s)):
#         return True
#     elif(count!=2):
#         return False
#     else:
#         if(s[i1]!=goal[i2] or s[i2]!=goal[i1]):
#             return False
#     return True


class Solution:
    def closeStrings(self, a: str, b: str) -> bool:
        if(len(a)!=len(b)):
            return False
        lena=len(a)
        lenb=len(b)
        seta=set()
        setb=set()
        mapa={}
        mapb={}
        for i in range(lena):
            seta.add(a[i])
            if (a[i] not in mapa):
                mapa[a[i]]=1
            else:
                mapa[a[i]]+=1
            setb.add(b[i])
            if(b[i] not in mapb):
                mapb[b[i]]=1
            else:
                mapb[b[i]]+=1
        if (seta!=setb):
            return False
        counta={}
        countb={}
        for item in mapa:
            if mapa[item] not in counta:
                counta[mapa[item]]=1
            else:
                 counta[mapa[item]]+=1
        for item in mapb:
            if mapb[item] not in countb:
                countb[mapb[item]]=1
            else:
                 countb[mapb[item]]+=1
        if(counta!=countb):
            return False
        return True