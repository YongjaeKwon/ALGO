import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split()))

dp_increase = [1 for _ in range(n)]
dp_decrease = [1 for _ in range(n)]

for i in range(n):
  for j in range(i):
    if arr[i] > arr[j]:
      dp_increase[i] = max(dp_increase[i], dp_increase[j] + 1)

for i in range(n-1,-1,-1):
  for j in range(n-1, i, -1):
    if arr[i] > arr[j]:
      dp_decrease[i] = max(dp_decrease[i], dp_decrease[j] + 1)

pivot = [0 for _ in range(n)]
for i in range(n):
  pivot[i] = dp_increase[i] + dp_decrease[i]

# 피봇이 중간에 겹치므로 -1
print(max(pivot)-1)