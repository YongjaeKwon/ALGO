import sys
input = sys.stdin.readline

k = int(input())
lst = list(input().split())
arr = [0 for _ in range(k+1)]
visited = [False for _ in range(10)]
fin = False

def check(cur):
  global fin
  if fin:
    return False
  if cur <= 1:
    return True
  if lst[cur-2] == '<' and arr[cur-2] > arr[cur-1]:
    return False
  if lst[cur-2] == '>' and arr[cur-2] < arr[cur-1]:
    return False
  return True

def recur(cur):
  global fin
  if not check(cur):
    return
  if cur == k + 1:
    fin = True
    str_ = ''
    for i in range(len(arr)):
      str_ += str(arr[i])
    print(str_)
    return
  for i in range(10):
    if visited[i]:
      continue
    visited[i] = True
    arr[cur] = i
    recur(cur+1)
    visited[i] = False

def recur_2(cur):
  global fin
  if not check(cur):
    return
  if cur == k + 1:
    fin = True
    str_ = ''
    for i in range(len(arr)):
      str_ += str(arr[i])
    print(str_)
    return
  for i in range(9,-1,-1):
    if visited[i]:
      continue
    visited[i] = True
    arr[cur] = i
    recur_2(cur+1)
    visited[i] = False

recur_2(0)
fin = False
recur(0)