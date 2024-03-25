import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]
dp = [[-1 for i in range(3)] for j in range(n)]


def recur(cur, prv):
  if cur == n:
    return 0
  
  if dp[cur][prv] != -1:
    return dp[cur][prv]
  
  ret = 1 << 60

  for i in range(3):
    if i == prv:
      continue

    ret = min(ret, recur(cur+1, i) + arr[cur][i])

  dp[cur][prv] = ret

  return dp[cur][prv]

print(recur(0, -1))