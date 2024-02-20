import sys
input = sys.stdin.readline

n, m = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]

min_ = sys.maxsize
chicken = []
house = []
def check(cur):
  return

def recur(cur):
  if cur == n:
    return
  for i in range(n):
    recur(cur+1)

for i in range(n):
  for j in range(n):
    if arr[i][j] == 2:
      chicken.append([i,j])
    elif arr[i][j] == 1:
      house.append([i,j])