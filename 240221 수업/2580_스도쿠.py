import sys
input = sys.stdin.readline

arr = [list(map(int,input().split())) for _ in range(9)]

def check(num, x,y):
  # 가로 점검
  if num in arr[x]:
    return False
  # 세로 점검
  for i in range(9):
    if num == arr[i][y]:
      return False
  # 네모칸 점검
  if 0<=x<=2:
    temp_x = 2
  elif 3<=x<=5:
    temp_x = 5
  else:
    temp_x = 8

  if 0<=y<=2:
    temp_y = 2
  elif 3<=y<=5:
    temp_y = 5
  else:
    temp_y = 8
  
  for i in range(temp_x-2,temp_x+1):
    for j in range(temp_y-2,temp_y+1):
      if i == x and j == y: 
        continue
      if num == arr[i][j]:
        return False
      
  return True

def recur(x,y):
  if y == 9:
    x += 1
    y = 0
  
  if x == 9:
    for i in range(9):
      print(*arr[i])
    exit()

  
  # 이미 채워져 있다면 넘어가기
  if arr[x][y] != 0:
    recur(x,y+1)
  # 빈칸이라면 한개씩 채워보면서 유효성 검사 후 재귀
  if arr[x][y] == 0:
    for num in range(1,10):
        if check(num,x,y):
          arr[x][y] = num
          recur(x,y+1)
          arr[x][y] = 0
          
recur(0,0)