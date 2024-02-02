class Solution:
    
    def largestNum(self, n, S):
        
        # code here
        ans = ''
        if n*9 < S :
            return -1
            
        while n > 0:
            while S > 9:
                ans += '9'
                S -= 9
                n -= 1
            
            ans += str(S)
            S = 0
            n -= 1

        # If there are still remaining digits, fill them with '0'
        ans += '0' * n
        
        

        return ans


                
            
                
                
        
    
    


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

#Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n,s = map(int,input().strip().split())
        ob = Solution()
        print(ob.largestNum(n,s))
# } Driver Code Ends