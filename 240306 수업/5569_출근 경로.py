import sys
input = sys.stdin.readline



def recur(cur, w, h, turn_after):
  if w > n or h > m:
    return 0
  
  if cur == n+m-2:
    return 1
  
  if dp[cur][w][h] != -1:
    return dp[cur][w][h]
  
  dp[cur][w][h] = recur(cur+1,w+1,h, turn_after) + recur(cur+1, w, h+1, turn_after)
  dp[cur][w][h] %= 100_000
  return dp[cur][w][h]



n, m = map(int,input().split())

dp = [[[-1 for _ in range(m+1)] for _ in range(n+1)] for _ in range(n+m+2)]

print(recur(0,0,0))