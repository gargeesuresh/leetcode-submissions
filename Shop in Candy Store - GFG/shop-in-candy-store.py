#User function Template for python3

class Solution:

    def candyStore(self, candies,N,K):
        # code here
        candies.sort()
        l=0
        r=N-1
        mini=0
        while(l<=r):
            mini+=candies[l]
            l+=1
            r-=K
        l=0
        r=N-1
        maxi=0
        while(l<=r):
            maxi+=candies[r]
            r-=1
            l+=K
        ans=(mini,maxi)
        return ans
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):

        N,K = [int(x) for x in input().split()]
        candies = [int(x) for x in input().split()]

        solObj = Solution()

        print(*solObj.candyStore(candies,N,K))
# } Driver Code Ends