'''
2차원 배열의 누적합 구하기
각 누적합 배열에는 왼쪽과 위쪽에있는 모든 누적합을 구한다.
'''
import sys
input = sys.stdin.readline
n,m = map(int,input().split())
arr = [[0]*(n+1)]
for i in range(n):
  arr.append([0]+list(map(int,input().split())))


prefix = list([0]*(n+1) for _ in range(n+1))
# 2차원 배열 누적합
for i in range(1,n+1):
  for j in range(1,n+1):
    prefix[i][j] = prefix[i][j-1] + prefix[i-1][j] - prefix[i-1][j-1] + arr[i][j]
for i in range(m):
  x1,y1,x2,y2 = map(int,input().split())
  ans = prefix[x2][y2] - prefix[x1-1][y2] - prefix[x2][y1-1] + prefix[x1-1][y1-1]
  print(ans)