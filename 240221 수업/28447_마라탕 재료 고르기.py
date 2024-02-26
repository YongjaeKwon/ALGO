import sys
input = sys.stdin.readline

n, k = map(int,input().split())
lst = [list(map(int,input().split())) for _ in range(n)]

arr = [0 for _ in range(n)]
max_ = -1*sys.maxsize

def check(arr,cnt):
  score = 0

  for i in range(cnt):
    for j in range(i+1, cnt):
      score += lst[arr[i]][arr[j]]

  return score

def recur(cur,cnt):
  global max_

  if cnt > k:
    return
  
  if cnt == k:
    temp = []

    for i in range(k):
      temp.append(arr[i])

    score = check(temp, k)
    max_ = max(score,max_)

  if cur == n:
    return
  
  recur(cur+1,cnt)
  arr[cnt] = cur
  recur(cur+1,cnt+1)

recur(0,0)
print(max_)