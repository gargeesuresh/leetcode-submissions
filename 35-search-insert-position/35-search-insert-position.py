class Solution:
    def searchInsert(self, n: List[int], t: int) -> int:
        l=0
        r=len(n)-1
        mid=l+int((r-l)/2)
        while(l<=r):
            if(n[mid]==t):
                return mid
            elif (n[mid]<t):
                l=mid+1
            else:
                r=mid-1
            mid=l+int((r-l)/2)
        return l