# Q2 : Generating sequence of the fibonnaci series
#https://leetcode.com/problems/generate-fibonacci-sequence/

class Solution:
    def fib(self, n: int) -> int: 
        if(n<0):
            return -1
        
        t = [-1 for _ in range(n)]
        t[0],t[1] = 0,1

        for i in range(2,n):
            t[i] = t[i-1]+t[i-2]
        return t
        
if __name__ == "__main__":
    solution = Solution()
    result = solution.fib(50)  
    print(result)

