'''
3명이 사탕을 나누는 방법
택희 영훈 남규 = x, y, z
사탕의 갯수 : N
조건!
1. x + y + z = N
2. z >= 2 + y
3. x != 0 and y != 0 and z != 0
4. x % 2 == 0
'''
import sys
input = sys.stdin.readline

N = int(input())

cnt = 0
for x in range(N + 1):
  for y in range(N + 1):
    for z in range(N + 1):
      if x + y + z != N:
        continue
      if z < 2 + y:
        continue
      if x == 0 or y == 0 or z == 0:
        continue
      if x % 2 == 1:
        continue
      cnt += 1
print(cnt)