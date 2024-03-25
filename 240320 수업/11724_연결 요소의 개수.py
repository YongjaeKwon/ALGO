import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(cur):

  visited[cur] = True

  for nxt in v[cur]:
    if visited[nxt]:
      continue

    dfs(nxt)


n, m = map(int,input().split())

v = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]

for i in range(m):
  x, y = map(int,input().split())
  v[x].append(y)
  v[y].append(x)

cnt = 0

for i in range(1,n+1):
  if visited[i]:
    continue

  cnt += 1
  dfs(i)

print(cnt)