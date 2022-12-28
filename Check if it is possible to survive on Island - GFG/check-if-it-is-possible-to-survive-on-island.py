#User function Template for python3

class Solution:
    def minimumDays(self, S, N, M):
        # code here
        if S>=7 and 6*N-7*M<0:
            return -1
        elif N<M:
            return -1
        if(S*M%N==0):
            return int(S*M/N)
        else:
            return int(S*M/N)+1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        S, N, M = [int(x) for x in input().split()]
        
        ob = Solution()
        print(ob.minimumDays(S, N, M))
# } Driver Code Ends