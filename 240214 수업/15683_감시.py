import sys
input = sys.stdin.readline
from copy import deepcopy
n, m = map(int,input().split())
lst = [list(map(int,input().split())) for _ in range(n)]
arr = deepcopy(lst)
cctv = []
search = [
  [],
  []
]

for i in range(n):
  for j in range(m):
    if lst[i][j] != 0 and lst[i][j] != 6:
      # cctv번호, 좌표
      cctv.append([lst[i][j],i,j])

min_ = sys.maxsize
def recur(cur):
  if cur == n:
    return
  # 4방향 탐색
  for i in range(4):
    arr[cur] = lst[i]
    recur(cur+1)