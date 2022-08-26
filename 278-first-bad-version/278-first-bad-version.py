# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l=1
        r=n
        mid=l+int((r-l)/2)
        while(r>=l):
            if(isBadVersion(mid)):
                if(mid-1==0 or (not isBadVersion(mid-1))):
                    return mid
                else:
                    r=mid-1
            else:
                l=mid+1
            mid=l+int((r-l)/2)