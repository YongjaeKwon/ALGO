import sys
input = sys.stdin.readline

n, k = map(int,input().split())
lst = list(map(int,input().split()))
rangee = [list(map(int,input().split())) for _ in range(k)]
merry = [list(map(int,input().split())) for _ in range(k)]

max_ = 0
def recur(cur,rang,merr):
  global max_
  if cur == k:
    max_ = max(max_, rang+merr)
    return
  for i in range(n):
    r , m = rang, merr
    if lst[i] > 0:
      lst[i] -= 1
      r += rangee[cur][i]
      for j in range(n):
        if lst[j] > 0:
          lst[j] -= 1
          m += merry[cur][j]
          recur(cur+1, r,m)
          m -= merry[cur][j]
          lst[j] += 1
      r -= rangee[cur][i]
      lst[i] += 1

recur(0,0,0)
print(max_)