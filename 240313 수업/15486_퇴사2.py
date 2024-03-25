import sys
input = sys.stdin.readline

# 바텀업 풀이
n = int(input())
arr = [[0,0]] + [list(map(int,input().split())) for _ in range(n)]
dp = [0 for _ in range(n+1)]

for i in range(1,n+1):
  # 이전 날짜까지의 최대값 할당
  dp[i] = max(dp[i], dp[i-1])
  # 끝나는 날짜
  date = i + arr[i][0] - 1
  if date <= n:
    dp[date] = max(dp[date], dp[i-1] + arr[i][1])

print(max(dp))