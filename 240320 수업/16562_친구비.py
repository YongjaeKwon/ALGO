import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(x):
  global cost

  visited[x] = True
  # 다른 친구를 먼저 사귀는게 더 싼 비용이라면 비용 갱신
  cost = min(cost, arr[x])
  #더 이상 타고갈 친구가 없다면
  if v[x] == []:
    return

  for nxt in v[x]:
    if visited[nxt]:
      continue

    visited[nxt] = True

    dfs(nxt)

n, m, k = map(int,input().split())
arr = [0] + list(map(int,input().split()))

v = [[] for _ in range(n+1)]

for i in range(m):
  x, y = map(int,input().split())
  v[x].append(y)
  v[y].append(x)

visited = [False for _ in range(n+1)]

answer = 0

for i in range(1,n+1):
  # 아직 탐색 안해본 친구 관계만 dfs
  if visited[i]:
    continue
  # i와 친구하는데 드는 비용
  cost = arr[i]
  dfs(i)
  answer += cost

if answer <= k:
  print(answer)
else:
  print("Oh no")