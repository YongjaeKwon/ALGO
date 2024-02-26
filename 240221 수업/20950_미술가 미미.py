import sys
input = sys.stdin.readline

n = int(input())
lst = [list(map(int,input().split())) for _ in range(n)]
gomdoori = list(map(int,input().split()))

min_ = sys.maxsize

def check(cnt, r, g, b):
  global min_

  moondoori = [r//cnt, g//cnt, b//cnt]
  
  return moondoori

def recur(cur, cnt, r, g, b):
  global min_

  if cnt > 7:
    return

  if cur == n:
    if cnt < 2:
      return
    
    di,dj,dk = check(cnt, r, g, b)
    i,j,k = gomdoori
    min_ = min(min_, abs(i - di) + abs(j - dj) + abs(k - dk))

    return

  dr, dg, db = lst[cur]
  recur(cur+1, cnt, r, g, b)
  recur(cur+1, cnt + 1, r + dr, g + dg, b + db)

recur(0,0,0,0,0)
print(min_)