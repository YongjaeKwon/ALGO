import sys
input = sys.stdin.readline

n, m = map(int,input().split())
lst = sorted(list(map(int,input().split())))
arr = [0 for _ in range(m)]

def check(cur):
  if cur <= 1:
    return True
  if arr[cur-2] >= arr[cur-1]:
    return False
  return True

def recur(cur):
  if not check(cur):
    return
  if cur == m:
    print(*arr)
    return
  for i in range(n):
    arr[cur] = lst[i]
    recur(cur + 1)

recur(0)