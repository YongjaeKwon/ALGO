import sys
input = sys.stdin.readline

def recur(cur, weight):

  if weight > k:
    return -10000000000
  
  if cur == n:
    return 0

  if dp[cur][weight] != -1:
    return dp[cur][weight]

  ret = recur(cur+1, weight + arr[cur][0]) +  arr[cur][1]
  dp[cur][weight] = max(ret, recur(cur+1, weight))

  return dp[cur][weight]


n, k = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]
dp = [[-1 for _ in range(100_010)] for _ in range(n)]

print(recur(0,0))
