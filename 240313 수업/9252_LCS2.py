import sys
input = sys.stdin.readline

arr1 = list(input().rstrip())
arr2 = list(input().rstrip())
n, m = len(arr1), len(arr2)
dp = [['' for _ in range(m+1)] for _ in range(n+1)]
for i in range(1, n+1):
  for j in range(1, m+1):
    if arr1[i-1] == arr2[j-1]:
      dp[i][j] = dp[i-1][j-1] + arr1[i-1]
    else:
      if len(dp[i][j-1]) >= len(dp[i-1][j]):
        dp[i][j] = dp[i][j-1]
      else:
        dp[i][j] = dp[i-1][j]

answer = dp[n][m]
print(len(dp[n][m]))

if len(dp) != 0:
  print(answer)