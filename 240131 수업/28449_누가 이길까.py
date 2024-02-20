'''
'''
import sys
input = sys.stdin.readline

n,m = map(int,input().split())
arr_a = list(map(int,input().split()))
arr_b = list(map(int,input().split()))
arr_a.sort()
arr_b.sort()

hi = 0
arc = 0
draw = 0

for a in arr_a:
  s = 0
  e = m - 1
  l = m
  # lowerbound 구하기
  while s <= e:
    mid = (s+e) //2
    if arr_b[mid] >= a:
      l = mid
      e = mid -1
    else:
      s = mid + 1
  # upperbound 구하기
  s = 0
  e = m - 1
  u = -1
  while s <= e:
    mid = (s+e) //2
    if arr_b[mid] <= a:
      u = mid
      s = mid + 1
    else:
      e = mid - 1
  
  hi += l
  arc += m - u - 1
  draw += u - l + 1
print(hi, arc, draw)