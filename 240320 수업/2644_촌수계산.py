import sys
input = sys.stdin.readline

def dfs(x,cnt):
  global answer

  visited[x] = True 

  if x == b:
    answer = cnt

  for nxt in v[x]:
    if visited[nxt]:
      continue

    dfs(nxt,cnt+1)


n = int(input())
a, b = map(int,input().split())
m = int(input())

v = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]
answer = -1

for i in range(m):
  x,y = map(int,input().split())
  v[x].append(y)
  v[y].append(x)

dfs(a,0)
print(answer)