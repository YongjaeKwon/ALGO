import sys
input = sys.stdin.readline

def dfs(x, start):
  global cnt
  
  visited[x] = True
  nxt = v[x]

  if not visited[nxt]:
    dfs(nxt,start)

  elif visited[nxt] and nxt == start:
    answer.append(nxt)

n = int(input())


v = [0] + list(int(input()) for _ in range(n))

cnt = 0
answer = []

for i in range(1,n+1):
  visited = [False for _ in range(n+1)]
  dfs(i, i)

answer.sort()

print(len(answer))
for ans in answer:
  print(ans)