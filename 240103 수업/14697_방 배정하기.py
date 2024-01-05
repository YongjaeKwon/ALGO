'''
3 종류의 방
같은방 종류 여러개
모든 방에 빈 침대가 없도록
가능하면 1 아니면 0
'''

import sys
input = sys.stdin.readline

A, B, C, N = map(int,input().split())

answer = 0
for x in range(N+1):
  for y in range(N-x+1):
    for z in range(N-x-y+1):
      if x%A == 0 and y%B == 0 and z%C == 0 and x+y+z == N:
        answer = 1

print(answer)