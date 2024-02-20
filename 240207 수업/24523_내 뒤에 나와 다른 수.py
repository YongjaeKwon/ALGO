import sys
input = sys.stdin.readline

n = int(input())
arr = [0] + list(map(int,input().split()))
answer = [-1] * (n+1)

# 맨 뒤에 index는 비교 대상이 없으므로 무조건 -1
idx = -1
for i in range(n,0,-1):
  answer[i] = idx
  # 가장 큰 j값을 찾는 것이기 때문에 뒤에서 부터 시작해서 idx값을 조정
  if arr[i-1] != arr[i]:
    # 최대 idx를 저장후 대입
    idx = i

for i in range(1,n+1):
  print(answer[i], end=' ')
