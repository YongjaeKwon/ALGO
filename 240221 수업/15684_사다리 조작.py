import sys
input = sys.stdin.readline

n, m, h = map(int,input().split())
lst = [[0]*n for _ in range(h)]

for i in range(m):
  a, b = map(int,input().split())
  lst[a-1][b-1] = 1

# 최대값 지정
answer = 3

def recur(cur, x, y):
  global answer

  if cur >= answer:
    return
  if check():
    answer = min(answer,cur)
    return
  
  if cur == 3:
    return
  
  for i in range(x,h):
    for j in range(y,h):
      if lst[i][j] == 0:
        lst[i][j] = 1
        recur(cur+1,i,j+2) # 연속된 가로선 방지하기 위해 2칸 건너 뜀.
        lst[i][j] = 0
    

recur(0,0,0)

if answer > 3:
  print(-1)
else:
  print(answer)