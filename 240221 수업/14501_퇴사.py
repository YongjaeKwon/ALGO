import sys
input = sys.stdin.readline

n = int(input())
lst = [0] + [list(map(int,input().split())) for _ in range(n)]

max_ = 0

def recur(cur,cnt,price):
  global max_

  if cur > n+1:
    return
  
  if cur == n+1:
    max_ = max(max_, price)
    return
  
  t, p = lst[cur]
  # 선택 안한다.
  recur(cur+1, cnt, price)
  # 선택 한다.
  recur(cur + t, cnt+1, price + p)

recur(1,0,0)
print(max_)