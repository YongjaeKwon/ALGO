import sys
input = sys.stdin.readline

def check(cur):
  if cur <= 1:
    return True
  if arr[cur-2] > arr[cur-1]:
    return False
  return True

def recur(cur):
  if not check(cur):
    return
  if cur == 6:
    print(*arr)
    return
  for i in range(k):
    if visited[i]:
      continue
    visited[i] = True
    arr[cur] = lst[i]
    recur(cur+1)
    visited[i] = False
  
while True:
  lst = list(map(int,input().split()))
  k = lst[0]
  if k == 0:
    break
  lst = lst[1::]
  arr = [0 for _ in range(6)]
  visited = [False for _ in range(k)]
  recur(0)
  print(' ')