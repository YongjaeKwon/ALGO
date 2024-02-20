import sys
input = sys.stdin.readline

n, m = map(int,input().split())
lst = sorted(list(map(int,input().split())))
visited = [False for _ in range(n)]
arr = [0 for _ in range(m)]
def recur(cur):
  if cur == m:
    print(*arr)
    return
  for i in range(n):
    if visited[i]:
      continue
    visited[i] = True
    arr[cur] = lst[i]
    recur(cur+1)
    visited[i] = False

recur(0)