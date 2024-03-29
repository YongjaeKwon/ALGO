import sys
input = sys.stdin.readline

def dfs(cur,x,y):
  global cnt

  visited[ord(arr[x][y])-65] = True
  cnt = max(cnt, cur)

  for i in range(4):
    nx, ny = x + dx[i], y + dy[i]
    if not (0<= nx < n and 0 <= ny < m):
      continue

    if visited[ord(arr[nx][ny])-65]:
      continue

    visited[ord(arr[nx][ny])-65] = True
    dfs(cur+1,nx,ny)
    visited[ord(arr[nx][ny])-65] = False

n, m = map(int,input().split())
arr = list(input().rstrip() for _ in range(n))

visited = [False for _ in range(26)]

dx, dy = [-1,1,0,0],[0,0,-1,1]

cnt = 0
dfs(1,0,0)

print(cnt)