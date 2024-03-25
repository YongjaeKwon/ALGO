import sys
input = sys.stdin.readline

T = int(input())
for i in range(T):
  n = int(input())
  arr = sorted([list(map(int,input().split())) for _ in range(n)])
  
  # 서류 1등은 무조건 합격
  cnt = 1
  max_ = arr[0][1]
  for j in range(1,n):
    interview = arr[j][1]
    # 숫자가 큰게 낮은 등수
    if max_ > arr[j][1]:
      cnt += 1
      max_ = arr[j][1]

  print(cnt)