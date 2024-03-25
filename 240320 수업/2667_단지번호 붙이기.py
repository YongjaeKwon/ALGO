import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(x,y):
	global cnt
	
	visited[x][y] = True
	cnt += 1
	
	for i in range(4):
		nx, ny = x + dx[i], y + dy[i]
		
		if not (0 <= nx < n and 0 <= ny < n) or arr[nx][ny] == '0':
			continue
		
		if visited[nx][ny]:
			continue
		
		dfs(nx,ny)			 
	
	

n = int(input())
arr = [input() for i in range(n)]
visited = [[False for _ in range(n)] for _ in range(n)]
cnt = 0
dx = [-1,1,0,0]
dy = [0,0,-1,1]
ans = []

for i in range(n):
	for j in range(n):
		if arr[i][j] == '0':
			continue
			
		if visited[i][j]:
			continue

		cnt = 0
		dfs(i,j)
		ans.append(cnt)
		
ans.sort()
		
print(len(ans))
for i in ans:
	print(i)