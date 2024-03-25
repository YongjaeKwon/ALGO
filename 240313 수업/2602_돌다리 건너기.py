'''
dp[i][j][k]
i : 현재위치
j : arr의 문자열 위치
k : 천사냐 악마냐 0: 악마 1: 천사
'''

import sys
input = sys.stdin.readline

arr = list(input())
devil = list(input())
angel = list(input())
m, n = len(arr), len(devil)

dp = [[[0 for _ in range(2)] for _ in range(m+1)] for _ in range(n+1)]

# dp 초기값 설정
for i in range(n):
  # 첫글자가 있으면 1로 바꿈
  if devil[i] == arr[0]:
    dp[i][0][0] = 1
  if angel[i] == arr[0]:
    dp[i][0][1] = 1

for i in range(n):
  for j in range(m):
    if devil[i] == arr[j]:
       for k in range(i):
         # 1~(i-1) 번째까지의 angel에서 마지막으로 기록된 j-1까지 완성된 경우의 수를 더한다.
         dp[i][j][0] += dp[k][j-1][1]
    if angel[i] == arr[j]:
       for k in range(i):
         # 1~(i-1) 번째까지의 devil에서 마지막으로 기록된 j-1까지 완성된 경우의 수를 더한다.
         dp[i][j][1] += dp[k][j-1][0]

# dp내에서 j == m인 모든 경우의 수를 더해야한다.
answer = 0
for i in range(n):
  answer += dp[i][m-1][0]
  answer += dp[i][m-1][1]

print(answer)