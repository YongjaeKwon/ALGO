'''
2차원 누적합배열에서 합이 0인 부분 배열중에서 가장 크기가 큰 배열 찾기.
=> 4중 for문 시간초과 
=> 최적화
0을 찾지 말고 해당 행의 누적합과 같은 y값이 있나 탐색.
=> y1,y2값을 고정해 가면서 행을 조절하는 방식
=> 만약 누적한 값이

'''
import sys
input = sys.stdin.readline
n,m = map(int,input().split())
arr = [[0]*(m+1)]
for i in range(n):
  temp = input().rstrip()
  temp_arr = []
  for j in temp:
    temp_arr.append(int(j))
  arr.append([0]+temp_arr)

prefix = list([0]*(m+1) for _ in range(n+1))
# 2차원 배열 누적합
for i in range(1,n+1):
  for j in range(1,m+1):
    prefix[i][j] = prefix[i][j-1] + prefix[i-1][j] - prefix[i-1][j-1] + arr[i][j]

answer = 0
# y값을 완전 탐색
for y1 in range(1,m+1):
  for y2 in range(y1,m+1):
    # 행을 1부터 시작
    x1 = 1
    # 부분 배열의 합을 담을 변수
    sum_ = 0
    # 끝 행을 조정하면서 부분 배열의 합이 sum_인 경우를 탐색
    for x2 in range(1,n+1):
      # 현재 탐색중인 y1부터 y2까지의 누적합
      temp = prefix[x2][y2] - prefix[x2][y1-1]
      # 부분배열의 합과 같다면 넓이 갱신
      if temp == sum_:
        answer = max(answer, (y2 - y1 + 1) * (x2 - x1 + 1))
      # 이전에 선택한 부분 배열보다 누적합이 크다.
      # x1을 업데이트하여 새로운 행을 선택.
      if temp > sum_:
        # 탐색할 행을 하나 늘린다.
        x1 = x2 + 1
      sum_ = temp
print(answer)