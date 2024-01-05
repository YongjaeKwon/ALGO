'''
두 근을 x , y라고 했을떄
두 근의 합은 -2A
두 근의 곱은 B

따라서 x + y = -2 * A
x * y = B

그렇다면 A와 B의 최소 최대를 이용해서 푼다면
1 , 1000
-1000 1
-1000 <= x * y <= 1000 => -1000 <= x, y <= 1000
-2000 <= x + y <= 2000 => -2000 <= x, y <= 2000
따라서 x,y 는 중복 범위인 -1000 <= x, y <= 1000 이 된다.
따라서 완전 탐색을 이용하여 풀게 된다면, -1000에서 1000까지 모두 대입해보면서 정답을 구할 수 있다. 
하지만 x, y가 바뀐 같은 쌍의 정답이 나올 수 있기 떄문에, 중복제거를 해준다.

'''

import sys
input = sys.stdin.readline

A,B = map(int,input().split())

answer = []
for x in range(-1000,1000):
  for y in range(-1000,1000):
    if x + y == -2*A and x * y == B:
      answer.append(x), answer.append(y)

answer = list(set(answer))
# 내림차순 정렬
answer.sort()
for i in answer:
  print(i, end=' ')