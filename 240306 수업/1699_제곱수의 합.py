import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n = int(input())
ans = 1 << 60
dp = [-1 for _ in range(n+10)]
# 기존 유형
def recur(cur, total):
  global ans

  if cur == n:
    ans = min(ans, total)
    return
  
  for i in range(1, n+1):
    if i * i > n - cur:
      break

    recur(cur+i*i, total + 1)

# recur(0,0)
# print(ans)

# ret를 안쪽에 저장함으로써 total 제거
def recur(cur):

  if cur == n:
    return 0
  
  ret = 1 << 60

  for i in range(1, n+1):
    if i*i > n - cur:
      break

    ret = min(ret, recur(cur+i*i) + 1)

  return ret

# print(recur(0))

# dp로 변형
def recur(cur):

  if cur == n:
    return 0
  
  if dp[cur] != -1:
    return dp[cur]
  
  ret = 1 << 60

  for i in range(1, n+1):
    if i*i > n - cur:
      break

    ret = min(ret, recur(cur+i*i) + 1)

  dp[cur] = ret

  return dp[cur]

print(recur(0))