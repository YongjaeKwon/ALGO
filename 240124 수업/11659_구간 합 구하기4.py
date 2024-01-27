'''
i번째 수부터 ~ j번쨰 수까지의 합을 구하여라
=> 구간의 get을 반복하는 문제.
=> 기본 누적합을 이용한다.
prefix는 앞에 0을 붙여두는게 편하다.
'''
import sys
input = sys.stdin.readline

N,M = map(int,input().split())
arr = list(map(int,input().split()))
arr = [0] + arr
prefix = [0] * (N+1)
for i in range(1,N+1):
  prefix[i] = prefix[i-1] + arr[i]
for _ in range(M):
  x, y = map(int,input().split())
  print(prefix[y] - prefix[x-1])