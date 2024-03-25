'''
두 지점이 통신하기 위해서는 한칸 떨어져 있어야한다.
한 지점이 고정되어있다 생각하고 출발지점이 끝까지 가는 경로를 모두 더한다.
예제에서 1 2 5 9의 경로에서
=> 1번에 있던 로봇이 2, 5 / or 9번에 있던 로봇이 5,2 로 가서 만나야한다.
=> 1-2 : 8 / 2-5 : 10 / 5-9 : 6
=> 2,5에서 만나는 것이 가장 효율적
=> 전체 거리에서 최대 거리를 빼주면 두 로봇이 통신할 수 있는 최소 거리.
'''
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(x, total_d, max_d):
  global answer

  visited[x] = True
  
  if x == end:
    answer = total_d - max_d
    return
  
  for nxt, d in v[x]:
    if visited[nxt]:
      continue

    dfs(nxt, total_d + d, max(d, max_d))


n, start, end = map(int,input().split())
v = [[] for _ in range(n+1)]

for i in range(n-1):
  x, y, d = map(int,input().split())
  v[x].append((y,d))
  v[y].append((x,d))

visited = [False for _ in range(n+1)]
answer = 1 << 60

dfs(start,0,0)
print(answer)