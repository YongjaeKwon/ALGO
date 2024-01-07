'''
1. 색종이를 2차원 배열로 구현해서 False로 채워 넣은 후, 해당 부분을 모두 True로 바꾸어 계산하는 방법
2. 특정 점이 어떤 사각형에 포함되어 있는지를 확인하는 방법.
'''
# # 풀이 1
# import sys
# input = sys.stdin.readline
# N = int(input())
# arr = []
# # 색종이 만들기
# paper = list([False for j in range(100)] for i in range(100))
# for i in range(N):
#   # 왼쪽 하단의 좌표를 입력 받는다.
#   x,y = map(int,input().split())
#   # 입력 받은 좌표에서 x + 10, y + 10 까지를 Paper에서 True로 바꿔준다.
#   for i in range(x,x+10):
#     for j in range(y,y+10):
#       paper[i][j] = True

# # 2차원 배열과 빈 배열을 더하면 해당 2차원 배열을 풀어헤칠 수 있다.
# answer = sum(paper,[]).count(True)
# print(answer)

# 풀이 2 (배열 없이)

import sys
input = sys.stdin.readline
N = int(input())

arr = []
for i in range(N):
  # 왼쪽 하단의 좌표를 입력 받는다.
  x,y = map(int,input().split())
  arr.append([x,y])

# 차지하고 있는 면접을 계산할 변수 cnt
cnt = 0
for i in range(100):
  for j in range(100):
    # 만들어진 모든 사각형에 포함되어 있는지 확인해야함.
    is_in_rectangle = False
    for rectangle in arr:
      x,y = rectangle
      # 사각형의 범위 안에 (i,j)가 존재한다면 True
      if x <= i < x + 10 and y <= j < y + 10:
        is_in_rectangle = True

    if is_in_rectangle == True:
      cnt += 1
print(cnt)