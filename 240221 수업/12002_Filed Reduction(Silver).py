'''
제외할 점 3개를 백트래킹으로 구한다.
조합 백트래킹 사용
'''

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
lst = [list(map(int,input().split())) for _ in range(n)]
# 제외할 index들을 담을 변수
arr = [0 for _ in range(n)]
min_ = sys.maxsize

def check(arr):
  global min_
  min_x, min_y, max_x, max_y = 40001, 40001, 0, 0
  for i in range(n):
    if i in arr:
      continue
    x, y = lst[i]
    min_x = min(x,min_x)
    min_y = min(y,min_y)
    max_x = max(x,max_x)
    max_y = max(y,max_y)
  min_ = min(min_, (max_x-min_x) * (max_y - min_y))

def recur(cur,cnt):
  if cnt > 3:
    return
  if cur == n:
    if cnt == 3:
      temp = arr[:cnt]
      check(temp)
    return
  
  arr[cnt] = cur
  recur(cur+1, cnt+1)
  recur(cur+1, cnt)

recur(0,0)
print(min_)