import sys
input = sys.stdin.readline

def dfs(x,y):
  global cnt
  
  visited[x][y] = True

  # 끝까지 도달 했다면 멈춘다.
  if y == m-1:
    cnt += 1
    return True

  # 위쪽부터 길이 열려있으면 탐색해야함. => 최대한 많은 파이프라인을 만들기 위해
  for dx in [-1,0,1]:
    nx = x + dx
    ny = y + 1
    
    if not (0 <= nx < n and 0 <= ny < m):
      continue

    if visited[nx][ny]:
      continue

    if not arr[nx][ny] == '.':
      continue

    visited[nx][ny] = True

    if dfs(nx,ny):
      return True
    
  return False

n, m = map(int,input().split())
arr = [list(input()) for _ in range(n)]

visited = [[False for _ in range(m)] for _ in range(n)]
cnt = 0

for i in range(n):
  dfs(i,0)

print(cnt)