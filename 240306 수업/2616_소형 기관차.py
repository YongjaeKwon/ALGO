import sys
input = sys.stdin.readline

# 1번 풀이
def recur(cur, train, total):
  global ans

  if cur > n or train > 3:
    return
  
  if cur == n:
    ans = max(ans, total)
    return
  
  recur(cur+1, train, total)
  if cur + m <= n:
    recur(cur+m, train + 1, total + prefix[cur+m] - prefix[cur])

# recur(0,0,0)
# print(ans)

# 2번 풀이
def recur(cur, train):
  if cur > n or train > 3:
    return -10000000

  if cur == n:
    return 0
  
  ret = - (1<<60)

  ret = max(recur(cur+1, train), recur(cur+m, train + 1)+ prefix[cur+m] - prefix[cur])

  return ret

# print(recur(0,0))

# 3번 풀이
def recur(cur, train):
  if cur > n or train > 3:
    return -10000000

  if cur == n:
    return 0
  
  if dp[cur][train] != -1:
    return dp[cur][train]

  dp[cur][train] = max(recur(cur+1, train), recur(cur+m, train + 1)+ prefix[cur+m] - prefix[cur])

  return dp[cur][train]


n = int(input())
arr = [0] + list(map(int,input().split()))
m = int(input())

# 범위 연산이 반복되는 이슈가 있어서 누적합을 사용
prefix = [0] * (n + 1) + [0] * m
for i in range(1,n+1):
  prefix[i] = prefix[i-1] + arr[i]

dp = [[-1 for i in range(4)] for j in range(n)] 
ans = -(1<<60)
print(recur(0,0))
