import sys
input = sys.stdin.readline

def dfs(cur):
  global cnt, visited
  
  visited[cur] = True
  cnt += 1

  for nxt in v[cur]:
    if visited[nxt]:
      continue

    dfs(nxt)

n = int(input())
m = int(input())

v = [[] for i in range(n+1)]
visited = [False for _ in range(n+1)]

for i in range(m):
  x, y = map(int,input().split())
  v[x].append(y)
  v[y].append(x)

cnt = 0
dfs(1)
print(cnt - 1)