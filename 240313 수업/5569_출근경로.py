import sys
input = sys.stdin.readline

n, m = map(int,input().split())

dp = [[[[0,0] for _ in range(2)] for _ in range(m)] for _ in range(n)]
print(dp)

for i in range(n):
  dp[i][0][0][1] = 1
for j in range(n):
  dp[0][i][0][1] = 1