import sys
input = sys.stdin.readline

n = int(input())

if n == 1:
  print(int(input()))
  exit()

arr = list(int(input()) for _ in range(n))

arr.sort()

max_ = arr.pop()
total = sum(arr)

if max_ >= total:
  answer = max_ - total

else:
  # 둘다 짝수라면
  if total % 2 == 0 and max_ % 2 == 0:
    answer = 0
  # 둘다 홀수라면
  elif total % 2 == 1 and max_ % 2 == 1:
    answer = 0
  # 홀 짝이라면
  else:
    answer = 1

print(answer)