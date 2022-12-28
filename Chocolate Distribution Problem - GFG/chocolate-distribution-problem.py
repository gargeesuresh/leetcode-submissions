#User function Template for python3
import sys
class Solution:

    def findMinDiff(self, A,N,M):
        A.sort()
        diff=sys.maxsize
        l=0
        r=M-1
        while(r<N):
            if diff>A[r]-A[l]:
                diff=A[r]-A[l]
            r+=1
            l+=1
        return diff
        # code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        N = int(input())
        A = [int(x) for x in input().split()]
        M = int(input())


        solObj = Solution()

        print(solObj.findMinDiff(A,N,M))
# } Driver Code Ends