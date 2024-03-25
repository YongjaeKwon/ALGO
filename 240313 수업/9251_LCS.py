import sys
input = sys.stdin.readline

arr1 = list(input().rstrip())
arr2 = list(input().rstrip())
n, m = len(arr1), len(arr2)
dp = [[0 for _ in range(m+1)] for _ in range(n+1)]

for i in range(1, n+1):
  for j in range(1, m+1):
    if arr1[i-1] == arr2[j-1]:
      # 같으면 최대 길이 +1
      dp[i][j] = dp[i-1][j-1] + 1
    else:
      # 다르면 이전에 있던 길이 중 최대
      dp[i][j] = max(dp[i][j-1], dp[i-1][j])

print(dp[n][m])
