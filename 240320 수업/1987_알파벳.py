import sys
input = sys.stdin.readline

def dfs(cur,x,y):
  global cnt

  visited[arr[x][y]] = True
  cnt = max(cnt, cur)

  for i in range(4):
    nx, ny = x + dx[i], y + dy[i]
    if not (0<= nx < n and 0 <= ny < m):
      continue

    if arr[nx][ny] in visited and visited[arr[nx][ny]]:
      continue

    visited[arr[nx][ny]] = True
    dfs(cur+1,nx,ny)
    visited[arr[nx][ny]] = False
    

n, m = map(int,input().split())
arr = list(input().rstrip() for _ in range(n))

visited = {}

dx, dy = [-1,1,0,0],[0,0,-1,1]

cnt = 0
dfs(1,0,0)

print(cnt)