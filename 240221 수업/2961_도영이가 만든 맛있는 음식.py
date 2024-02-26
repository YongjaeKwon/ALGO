import sys
input = sys.stdin.readline

n = int(input())
lst = [list(map(int,input().split())) for _ in range(n)]

min_ = sys.maxsize

def check(sour,bitter):
  global min_

  min_ = min(min_,abs(sour - bitter))
  return

def recur(cur,cnt,sour,bitter):
  global min_

  if cur == n:
    if cnt != 0:
      check(sour,bitter)
    return
  
  temp_s, temp_b = lst[cur]

  recur(cur+1, cnt, sour, bitter)
  recur(cur+1, cnt + 1, sour*temp_s, bitter+temp_b)
  
recur(0,0,1,0)

print(min_)