import sys
input = sys.stdin.readline
a,b = map(int,input().split())

lst = []

temp = a
while True:
  div, mod = divmod(temp,10)
  lst.append(mod)
  temp = div
  if div == 0:
    break

n = len(lst)
arr = [0 for _ in range(n)]
visited = [False for _ in range(n)]
answer = -1
def check():
  global answer
  temp = 0
  if arr[0] == 0:
    return
  for i in range(n):
    temp += arr[i]* (10**(n-1-i))
  if temp < b:
    answer = max(temp,answer)
  return
def recur(cur):
  if cur == n:
    check()
    return
  for i in range(n):
    if visited[i]:
      continue
    visited[i] = True
    arr[cur] = lst[i]
    recur(cur+1)
    visited[i] = False
    
recur(0)
print(answer)