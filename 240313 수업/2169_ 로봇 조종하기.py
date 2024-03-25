import sys
input = sys.stdin.readline

n, m = map(int, input().strip().split())
arr = [list(map(int, input().split())) for i in range(n)]

dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
dp[1][1] = arr[0][0]

# 맨 윗줄의 경우 오른쪽으로 이동하는 경우밖에 없다.
for i in range(2,m+1):
  dp[1][i] = dp[1][i-1] + arr[0][i-1]

# 왼쪽에서 오는값, 오른쪽에서 오는값을 비교해야한다. (각각 위에서 내려오는 값들이랑 비교하면서 갱신)
for i in range(2, n+1):
    # print(dp)
    left = [0 for _ in range(m+2)]
    right = [0 for _ in range(m+2)]
    # 왼쪽에서 오는값과 위에서 오는값 비교
    # 왼쪽 초기값.
    left[0] = dp[i-1][1]
    for j in range(1, m+1):
        left[j] = max(left[j-1], dp[i-1][j]) + arr[i-1][j-1]
    
    # 오른쪽에서 오는 값과 위에서 오는값 비교
    # 오른쪽 초기값
    right[m+1] = dp[i-1][m]
    for j in range(m, 0, -1):
        right[j] = max(right[j+1], dp[i-1][j]) + arr[i-1][j-1]
    # print(left, right)

    # 최종 비교
    for j in range(1, m+1):
        dp[i][j] = max(left[j], right[j])

# print(dp)
print(dp[n][m])