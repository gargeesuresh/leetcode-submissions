# User function Template for python3
def swap(S,l,r):
    r=r-1
    if len(l==r) <= 1:
            return
    mid = S[l+1:]
    return str[len(str) - 1] + mid + str[0]
    return S
class Solution:
    
    #Function to reverse words in a given string.
    def reverseWords(self,S):
        # code here 
        words=S.split(".")
        return ".".join(words[::-1])
    
    
            
            

#{ 
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        s = str(input())
        obj = Solution()
        print(obj.reverseWords(s))

# } Driver Code Ends