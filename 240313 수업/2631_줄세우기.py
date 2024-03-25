'''
최소로 움직이려면, 가장 긴 부분 수열을 구한 후에 나머지 친구들만 이동시켜주면 된다.
'''

import sys
input = sys.stdin.readline

n = int(input())
arr = list(int(input()) for _ in range(n))

dp = [1 for _ in range(n)]

for i in range(n):
  for j in range(i):
    if arr[i] > arr[j]:
      dp[i] = max(dp[i], dp[j]+1)

print(n - max(dp))