'''
모든 좌표들에 대해서 (x,y), (x,y+b), (x+a,y), (x+a,y+b)가 존재하는지 확인 후 cnt +1
=> list로 조회시 O(n)이 소모된다
=> set으로 조회시 O(1)이 소모된다.
'''
import sys
input = sys.stdin.readline

# 점들의 개수
n = int(input())
# 가로길이 세로길이
a,b = map(int,input().split())
# 좌표
arr = []
for _ in range(n):
  arr.append(tuple(map(int,input().split())))
arr = set(arr)
cnt = 0
for xy in arr:
  x, y = xy
  if (x + a, y) in arr and (x, y+b) in arr and (x+a,y+b) in arr:
    cnt += 1
  
print(cnt)