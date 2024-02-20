import sys
input = sys.stdin.readline

n, m = map(int,input().split())
arr = [0 for _ in range(m)]

def recur(cur,start):
  if cur == m:
    print(*arr)
    return
  for i in range(start,n+1):
    arr[cur] = i
    recur(cur + 1, i + 1)

recur(0,1)