'''
'''
import sys
input = sys.stdin.readline
n,m = map(int,input().split())
arr = [[0]*(m+1)]
for i in range(n):
  arr.append([0]+list(map(int,input().split())))


prefix = list([0]*(m+1) for _ in range(n+1))
# 2차원 배열 누적합
for i in range(1,n+1):
  for j in range(1,m+1):
    prefix[i][j] = prefix[i][j-1] + prefix[i-1][j] - prefix[i-1][j-1] + arr[i][j]

answer = -1 * sys.maxsize
for x1 in range(1,n+1):
  for y1 in range(1,m+1):
    for x2 in range(x1,n+1):
      for y2 in range(y1,m+1):
        temp = prefix[x2][y2] - prefix[x1-1][y2] - prefix[x2][y1-1] + prefix[x1-1][y1-1]
        answer = max(answer,temp)

print(answer)