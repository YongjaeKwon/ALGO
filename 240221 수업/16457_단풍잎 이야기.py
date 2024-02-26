import sys
input = sys.stdin.readline

def recur(cur,cnt):
  global max_quest

  if cnt > n:
    return
  
  if cnt == n:
    temp = []
    for i in range(cnt):
      temp.append(arr[i])

    quest = 0
    for i in range(m):
      a = lst[i]
      flag = 0
      for j in range(k):
        if a[j] in temp:
          flag += 1
      if flag == k:
        quest += 1

    max_quest = max(max_quest, quest)
  
  if cur == 2*n:
    return
  
  recur(cur+1,cnt)
  arr[cnt] = cur + 1
  recur(cur+1,cnt+1)

n, m, k = map(int,input().split())
lst = [list(map(int,input().split())) for _ in range(m)]
arr = [0 for _ in range(2*n + 1)]
max_quest = 0

recur(0,0)
print(max_quest)