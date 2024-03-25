import sys
input = sys.stdin.readline

# m: 움직인 횟수: 시간
n, m = map(int,input().split())


arr = [0] + [int(input()) for _ in range(n)]

dp = [[0 for _ in range(m+1)] for _ in range(n+1)]

for i in range(1, n+1):
  # 1번 나무에 가만히 서있을 경우 => 움직임 0 1번 나무에서 떨어지는거 계속 받아먹기
  if arr[i] == 1:
    dp[i][0] = dp[i-1][0] + 1

  for j in range(1, m+1):
    # 시작이 1번위치 => 1번 움직이면 2번나무, 2번 움직이면 1번나무 => 나머지로 위치를 계산한다.
    # 1번 위치에 있으면서 받아먹는 방법. => 움직여서 먹거나, 안움직이면서 먹거나 => + 1
    # 2번 위치에 서있으면서 받아먹는 방법 => 움직여서 먹거나, 안움직이면서 먹거나 => + 1
    # => 조건문만 다르고 dp를 채워나가는 방식은 똑같다.
    if (arr[i] == 1 and j%2 == 0) or (arr[i] == 2 and j%2 == 1):
      dp[i][j] = max(dp[i-1][j], dp[i-1][j-1]) + 1

    # 안받아먹기 => 움직여서 안먹거나, 가만히 있어서 안먹거나
    else:
      dp[i][j] = max(dp[i-1][j], dp[i-1][j-1])

# n초후 최대로 받아먹은 자두의 갯수 => dp[n]의 최대값
print(max(dp[n]))