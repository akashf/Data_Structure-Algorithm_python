print('hello Python workbook')
m,n = 3,7
t = [[0 for i in range(0,n)] for x in range(0,m)]

# [[0, 0, 0, 0, 0, 0, 0],
#  [0, 0, 0, 0, 0, 0, 0],
#  [0, 0, 0, 0, 0, 0, 0]]

for i in range(0,m):
    for j in range(0,n):
        if i == 0:
            t[i][j] = 1
        if j == 0:
            t[i][j] = 1


# [[1, 1, 1, 1, 1, 1, 1],
#  [1, 0, 0, 0, 0, 0, 0],
#  [1, 0, 0, 0, 0, 0, 0]]

for i in range(1,m):
    for j in range(1,n):
      t[i][j] =  t[i-1][j] + t[i][j-1]

print(t[m-1][n-1])
# [[1, 1, 1, 1, 1, 1, 1],
#  [1, 2, 3, 4, 5, 6, 7],
#  [1, 3, 6, 10, 15, 21, 28]]