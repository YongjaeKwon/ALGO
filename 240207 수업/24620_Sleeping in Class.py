import sys
input = sys.stdin.readline

def check(x):
  sum_ = 0
  for i in range(n):
    # 합쳤을때 타겟보다 커지면 False (합칠 수 없음)
    if sum_ > x:
      return False
    sum_ += arr[i]
    # 가능한 경우 그 다음 숫자부터 다시 x가 될 수 있는지 확인을 위해 초기화
    if sum_ == x:
      sum_ = 0
    # 남은애들은 확인할 필요가 없음. 불가능하다면 결국 1개로 합쳐질것이기 때문.
  return True

T = int(input())
for _ in range(T):
  n = int(input())
  arr = list(map(int,input().split()))

  # 전체 합.
  total = sum(arr)
  # 합쳐야하는 최소 크기
  min_sum = max(arr)

  # 0으로 나누어야하는 경우 예외처리
  if min_sum == 0:
    min_sum = 1

  move_cnt = 0
  # 내가 합칠 수 있는 숫자들 범위
  for i in range(min_sum,total+1):
    # 합칠 수 있는 숫자인지 & 그 숫자로 합칠 수 있는지 확인
    if total%i == 0 and check(i):
      move_cnt = n - total//i
      break
  print(move_cnt)