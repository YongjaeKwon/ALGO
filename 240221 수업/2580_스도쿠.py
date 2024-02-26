import sys
input = sys.stdin.readline

lst = [list(map(int,input().split())) for _ in range(9)]

arr = [[0 for i in range(9)] for j in range(9)]
visited = [False for _ in range(10)]


def recur(x,y):
  if y == 9:
    x += 1
    y = 0
  
  if x == 9:
    return
  
  for i in range(1,10):
    for j in range(1,10):
      if arr[i][j] == 0:
        