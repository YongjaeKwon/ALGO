import sys
input = sys.stdin.readline

n, k = map(int,input().split())
arr = list(int(input()) for _ in range(n))
dp = [0 for _ in range(k+1)]

# 0원을 만드는 경우의 수는 1
dp[0] = 1
for i in arr:
  for j in range(i, k+1):
    # j-i원을 만드는 경우의 수를 더한다.
    dp[j] += dp[j-i]

print(dp[k])