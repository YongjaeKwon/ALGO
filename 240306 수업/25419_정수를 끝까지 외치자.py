import sys
input = sys.stdin.readline

n, k = map(int,input().split())
arr = set(list(map(int,input().split())))
dp = [[-1 for i in range(2)] for j in range(n)]

ans = 0

def recur(player, value):

  if value > n:
    return False
  
  if dp[value] != -1:
    return dp[value]
  
  ret = True

  for i in range(value+1, min(value+k, n)+1):
    if i in arr:
      break
    recur(cur+1, i, cur%2)


recur(1, ,0)