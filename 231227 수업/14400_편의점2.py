'''
x축과 y축은 독립이다.
따라서 최선인 x 와 최선인 y를 찾는것이 최선의 방법이다.
안테나와 마찬가지로 홀수이면 중앙값
짝수라면 중앙값 범위 내에 아무데나 다 상관이 없다. (최소값으로 풀 예정)
'''

import sys
input = sys.stdin.readline

N = int(input())
X = []
Y = []
for _ in range(N):
  x, y = map(int,input().split())
  X.append(x)
  Y.append(y)
# 중앙값을 찾기위해 정렬한다.
X.sort()
Y.sort()
# 각 x좌표와 y좌표의 중간을 찾아내는게 최소 거리가 될 것이다.
# 좌표가 짝수일 때
if N%2 == 0:
  index = N//2 -1
# 좌표가 홀수일 때
else:
  index = N//2

X_center = X[index]
Y_center = Y[index]

# 최종으로 구할 거리
distance = 0
# 모든 좌표를 돌며 거리를 계산 (절대값)
for i in range(N):
  # X좌표 거리
  distance += abs(X_center - X[i])
  # Y좌표 거리
  distance += abs(Y_center - Y[i])

print(distance)