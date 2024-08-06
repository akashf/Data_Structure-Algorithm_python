# numRows = 500
# listar = [[1],[1,1]]
# # for i in range(2,numRows):
# #     arr = list()
# #     k = 0
# #     for j in range(0,i+1):
# #         if(j == 0 or j == i):
# #             arr.append(1)
# #         else:
# #             arr.append(listar[i-1][k]+listar[i-1][k+1])
# #             k = k+1
# #     listar.append(arr)
# print(listar[1:len(listar)])


cost = [1,3,2,2,1]
n = len(cost)

candy = [1 for _ in range(0,n)]

for i in range(1, n-1):
    if(cost[i-1]< cost[i]):
        print("yes", cost[i])
        candy[i] = candy[i]+1
    
    
print(candy)