import sys
input = sys.stdin.readline
n = int(input())
arr = [0] + list(map(int,input().split()))
prefix = [0] * (n + 1)

for i in range(1,n+1):
  prefix[i] = prefix[i-1] + arr[i]

subtract = sys.maxsize
answer = 0

# 모든 i를 기점으로 왼쪽 오른쪽을 구함
for i in range(1, n + 1):
  s = i
  e = i + 1
  while s > 0 and e <= n:
    # 왼쪽 오른쪽의 합을 구해서 차이를 비교
    sum_left = prefix[i] - prefix[s - 1]
    sum_right = prefix[e] - prefix[i]
    # 최소값이 갱신되면
    if subtract > abs(sum_right - sum_left):
      subtract = abs(sum_right - sum_left)
      # s~e까지의 학생들에게 steak 부여
      answer = prefix[e] - prefix[s - 1]
    # 최소값이 같다면 합이 더 큰 그룹에게 부여
    elif subtract == abs(sum_right - sum_left):
      answer = max(answer, prefix[e] - prefix[s - 1])

    # 두 그룹의 크기를 변경해가면서 비교한다.
    if sum_left >= sum_right:
      e += 1
    else:
      s -= 1

print(answer)