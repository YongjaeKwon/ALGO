import sys
input = sys.stdin.readline

n = int(input())
lst = [list(map(int,input().split())) for _ in range(n)]
arr = [0 for _ in range(5)]
visited = [False for _ in range(n)]

max_ = 0

def check():
  global max_
  temp = 0
  for i in range(5):
    temp += lst[arr[i]][i]
  max_ = max(max_,temp)


def recur(cur):
  global max_
  if cur == 5:
    check()
    return
  for i in range(n):
    if visited[i]:
      continue
    visited[i] = True
    arr[cur] = i
    recur(cur+1)
    visited[i] = False

recur(0)
print(max_)