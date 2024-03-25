'''
LCS응용하기...!
원본 배열과 뒤집은 배열의 최장 공통수열을 찾는다
=> 모자란 부분을 채워주면 된다......!
=> n - 최장 공통수열 길이 ==> 모자란 부분
'''
import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split()))
arr_r = arr[::-1]
dp = [[0 for _ in range(n+1)] for _ in range(n+1)]

for i in range(1, n+1):
  for j in range(1, n+1):
    if arr[i-1] == arr_r[j-1]:
      # 같으면 최대 길이 +1
      dp[i][j] = dp[i-1][j-1] + 1
    else:
      # 다르면 이전에 있던 길이 중 최대
      dp[i][j] = max(dp[i][j-1], dp[i-1][j])

print(n - dp[n][n])