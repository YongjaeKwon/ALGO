import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# row : 연속으로 선인장이 몇번 등장 했는지.
# cnt : 높이가 2인 선인장이 연속으로 몇개 있는지.
# two : 높이가 2인 선인장이 설치 됐는지.
def recur(cur, row, cnt, two):
  if row > 2 or cnt >=2:
    return 0
  
  if cur == n:
    if two:
      return 1
    else:
      return 0

  if dp[cur][row][cnt][two] != -1:
    return dp[cur][row][cnt][two]
  # 아무 선인장도 놓지 않는거 + 높이가 1인 선인장 놓기 + 높이가 2인 선인장 놓기
  dp[cur][row][cnt][two] = recur(cur+1,0,0,two) + recur(cur+1, row+1, 0, two) + recur(cur+1, row+1, cnt+1, 1)
  dp[cur][row][cnt][two] %= 1_000_000_007

  return dp[cur][row][cnt][two]
  
n = int(input())
dp = [[[[-1 for i in range(2)] for _ in range(2)] for _ in range(3)] for _ in range(n)]

# cur을 1로 시작함으로써 0번 자리에 장애물을 놓는 것을 방지
print(recur(1,0,0,0))