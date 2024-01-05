'''
A의 제곱은 B의 제곱보다 N 만큼 크다.
A제곱에서 B제곱을 빼면 N이다.
'''
import sys
input = sys.stdin.readline

N = int(input())

cnt = 0
for b in range(1,501):
  for a in range(b,501):
    if a**2 - b**2 == N:
      cnt += 1
print(cnt)