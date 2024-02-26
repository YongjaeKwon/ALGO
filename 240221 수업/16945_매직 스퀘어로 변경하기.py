import sys
input = sys.stdin.readline

lst = [list(map(int,input().split())) for _ in range(3)]

arr = [[0 for i in range(3)] for j in range(3)]
visited = [False for _ in range(10)]

min_ = sys.maxsize

def check():
  # 가로 합
  for i in range(3):
    total = 0
    for j in range(3):
      total += arr[i][j]
    if total != 15:
      return False
  
  # 세로 합
  for j in range(3):
    total = 0
    for i in range(3):
      total += arr[i][j]
    if total != 15:
      return False
    
  # 대각선 합
  if arr[0][2] + arr[1][1] + arr[2][0] != 15:
    return False 
  if arr[0][0] + arr[1][1] + arr[2][2] != 15:
    return False 
  
  return True


def recur(x,y,price):
  global min_

  if y == 3:
    x += 1
    y = 0
  
  if x == 3:
    if not check():
      return
    
    min_ = min(min_,price)
    return
  
  for i in range(1,10):
    if visited[i]:
      continue

    visited[i] = True
    arr[x][y] = i
    recur(x, y+1, price + abs(lst[x][y] - i))
    visited[i] = False

recur(0,0,0)

print(min_)