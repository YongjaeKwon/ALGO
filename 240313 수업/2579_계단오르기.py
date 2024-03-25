import sys
input = sys.stdin.readline

n = int(input())
arr = [0 for _ in range(310)]
for i in range(1,n+1):
  arr[i] = int(input())

dp = [0 for _ in range(310)]

dp[1] = arr[1]
dp[2] = arr[1] + arr[2]
# 연속 3계단을 밟을 수 없으니, 1번 밟고 3번밟기 or 2,3번 밟기
dp[3] = max(arr[1]+arr[3], arr[2]+arr[3])
'''
dp[4] = arr[1] + arr[3] + arr[4] , arr[1] + arr[2] + arr[4]
dp[4] = dp[1] + arr[3] + arr[4] , dp[2] + arr[4]

=> dp[i] = dp[i-3] + arr[i-1] + arr[i] , dp[i-2] + arr[i]
'''
if n < 4:
  print(dp[n])
  exit()


for i in range(4, n+1):
  dp[i] = max(dp[i-3] + arr[i-1] + arr[i], dp[i-2] + arr[i])

print(dp[n])