import sys
input = sys.stdin.readline

n = int(input())
arr = [0 for _ in range(n)]
visited = [False for _ in range(n)]
cnt = 0
def check(cur):
  for i in range(cur):
    if arr[cur] == arr[i]:
      return False
    if cur-i == abs(arr[cur]-arr[i]):
      return False
  return True

def recur(cur):
  global cnt
  if cur == n:
    cnt += 1
    return
  for i in range(n):
    arr[cur] = i
    if check(cur):
      recur(cur+1)

recur(0)
print(cnt)