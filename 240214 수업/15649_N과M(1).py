import sys
input = sys.stdin.readline

n, m = map(int,input().split())
arr = [0 for i in range(m)]
visited = [False for _ in range(n+1)]
def recur(cur):
  if cur == m:
    print(*arr)
    return
  
  for i in range(1,n+1):
    if visited[i]:
      continue
    visited[i] = True
    arr[cur] = i
    recur(cur + 1)
    visited[i] = False

recur(0)