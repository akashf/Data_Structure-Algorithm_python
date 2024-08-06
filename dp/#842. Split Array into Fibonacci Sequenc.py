#1414. Find the Minimum Number of Fibonacci Numbers Whose Sum Is K


class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        if k <0:
            return -1
        elif k <2:
            return k
        arr = [1,1]
        for i in range(2,k+1):
            temp = arr[i-1]+arr[i-2]
            if temp <= k:
                arr.append(temp)
            else:
                break
        return arr
    
    #recursion
    # def minsubsetsum(self, arr, n, w):
    #         if w == 0:
    #             return 0
    #         if n == 0:
    #             return float('inf')
    #         if(arr[n-1] <= w):
    #             return min(1 + self.minsubsetsum(arr, n-1, w-arr[n-1]),self.minsubsetsum(arr,n-1,w))
    #         elif(arr[n-1]>w):
    #             return self.minsubsetsum(arr, n-1, w)

    #dp
    def minsubsetsum(self, arr, n, w):
            r = n+1
            c = w+1
            t = [[float('inf') for _ in range(c)] for _ in range(r)]
            for i in range(r):
                t[i][0] = 0

            for i in range(1,r):
                for j in range(1,c):
                    if(arr[i-1] <= j):
                        t[i][j] = min(1+t[i][j - arr[i-1]] , t[i-1][j])
                    else:
                        t[i][j] = t[i-1][j]
            return t[n][w]

if __name__ == "__main__":
    solution = Solution()
    w = 7
    arr = solution.findMinFibonacciNumbers(w)  
    print(arr)
    result = solution.minsubsetsum(arr,len(arr),w)  
    print(result)


# Dp solution :



