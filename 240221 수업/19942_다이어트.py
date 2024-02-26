import sys
input = sys.stdin.readline

n = int(input())
mp, mf, ms, mv = map(int,input().split())
lst = [list(map(int,input().split())) for _ in range(n)]

arr = [0 for _ in range(n)]
answer = []
min_ = sys.maxsize

def check(p, f, s, v, price):
  global mp, mf, ms, mv, min_

  if price > min_:
    return False
  
  if p < mp or f < mf or s < ms or v < mv:
    return False
  return True

def recur(cur, cnt, p, f, s, v, price):
  global mp, mf, ms, mv, min_, answer

  if price > min_:
    return

  if cur == n:
    if not check(p, f, s, v, price):
      return
    
    if price < min_:
      answer = []

    min_ = min(min_, price)

    temp = []
    for i in range(cnt):
      temp.append(arr[i])

    answer.append(temp)
    return
  
  dp, df, ds, dv, dprice = lst[cur]
  type = cur+1
  arr[cnt] = type

  recur(cur+1, cnt + 1, p + dp, f + df, s + ds, v + dv, price + dprice)
  recur(cur+1, cnt, p, f, s, v, price)

recur(0,0,0,0,0,0,0)

if min_ == sys.maxsize:
  print(-1)
  print()

else:
  answer.sort()

  print(min_)
  print(*answer[0])