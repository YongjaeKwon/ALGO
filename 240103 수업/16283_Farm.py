'''
양 한마리는 사료를 a만큼
염소 한마리는 b만큼 먹는다

염소와 양의 전체 숫자는 알고 있음. = n마리
전체 먹는 사료의 양도 알고 있음. = w

입력으로 a b n w 가 주어진다.

양은 x, 염소는 y

x + y = n
a * x + b * y = w

가능한 해가 2개 이거나, 없을 경우 -1을 출력한다.
1 ≤ a ≤ 1,000, 1 ≤ b ≤ 1,000, 2 ≤ n ≤ 1,000, 2 ≤ w ≤ 1,000,000 이기 때문에 각각 한 마리 이상, 합쳐서 1000마리 이하이다.
'''
'''
# 풀이 1
import sys
input = sys.stdin.readline

a, b, n ,w = map(int,input().split())
answer = []
for x in range(1,1001):
  for y in range(1,1001):
    if x + y == n and a * x + b * y == w:
      answer.append((x,y))

if answer == [] or len(answer) >= 2:
  print(-1)
else:
  x, y = answer.pop()
  print(x, y)
'''

# 풀이 2
import sys
input = sys.stdin.readline

a, b, n ,w = map(int,input().split())

answer = []
for x in range(1,1001):
  y = n - x
  # 이 경우 y가 1 이상이라는 조건이 필요하다.
  if x + y == n and a * x + b * y == w and y >= 1:
    answer.append((x,y))

if answer == [] or len(answer) >= 2:
  print(-1)
else:
  x, y = answer.pop()
  print(x,y)
