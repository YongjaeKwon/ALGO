import sys
input = sys.stdin.readline

n = int(input())
# 전깃줄이 꼬이지 않으려면 일단 정렬된 상태에서 조건을 달아야한다.
arr = sorted([list(map(int,input().split())) for _ in range(n)])
dp = [1 for _ in range(n)]

for i in range(n):
  for j in range(i):
    # 비교하려는 전깃줄이 더 크다면, 꼬이기 때문에 넘어간다.
    if arr[i][1] < arr[j][1]:
      continue
    dp[i] = max(dp[i], dp[j]+1)

# 남아있는 전깃줄 구하기
print(n - max(dp))