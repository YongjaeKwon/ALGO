'''
12
1 2 3
4 5 6
7 8 9
10 11 12
13 14 15
16 17 18
19 20 21
22 23 24
25 26 27
28 29 30
31 32 33
34 35 36
255 255 255
'''

import sys
input = sys.stdin.readline

n = int(input())
lst = [list(map(int,input().split())) for _ in range(n)]
r,g,b = list(map(int,input().split()))
m = n if n < 7 else 7
arr = [[0,0,0] for _ in range(m)]


min_ = sys.maxsize
def check(cur,arr):
  global r,g,b
  global min_
  mr, mg, mb = 0, 0, 0
  for i in range(len(arr)):
    mr += arr[i][0]
    mg += arr[i][1]
    mb += arr[i][2]
  mr //= cur
  mg //= cur
  mb //= cur
  moondoori = abs(r-mr) + abs(g-mg) + abs(b-mb)
  min_ = min(moondoori, min_)
  return
  
def recur(cur,start,cnt):
  global min_
  if cur == cnt:
    check(cur,arr)
    return
  for i in range(start,n):
    arr[cur] = lst[i]
    recur(cur+1,i+1,cnt)
for cnt in range(2,m+1):
  recur(0,0,cnt)
print(min_)