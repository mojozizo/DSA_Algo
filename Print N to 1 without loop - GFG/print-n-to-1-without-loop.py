#User function Template for python3

class Solution:
    def printNos(self, n):
        # Code here
        def Recursion(n):
            if (n > 0 ):
                print(n, end=" ")
                n = n - 1
                Recursion(n)
            
            return 
        return Recursion(n)

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ob.printNos(N)
        print()
# } Driver Code Ends