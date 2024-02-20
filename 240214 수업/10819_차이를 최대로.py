import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int,input().split()))
arr = [0 for _ in range(n)]
visited = [False for _ in range(n)]

max_ = -1 * sys.maxsize
def check(arr):
  global max_
  temp = 0
  for i in range(n-1):
    temp += abs(arr[i] - arr[i+1])
  max_ = max(temp,max_)
  return

def recur(cur):
  global max_
  if cur == n:
    check(arr)
    return
  for i in range(n):
    if visited[i]:
      continue
    visited[i] = True
    arr[cur] = lst[i]
    recur(cur+1)
    visited[i] = False

recur(0)
print(max_)