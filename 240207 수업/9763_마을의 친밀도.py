'''
N = 10000
2중 for문으로 풀어야함.
완탐 :
1.  
i j k 마을의 거리를 구해서 최소 친밀도를 구한다.
3 중 for문 탈락
2. 
조합을 구해서 NC3의 경우의 수에 대해서 구한다.
=> 10000* 9999 * 9998 / 3*2*1
=> 시간초과
각 마을의 거리를 구해서 최소값과 2번째 최소값을 갱신한다.
'''
import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]

answer = sys.maxsize

# 마을 두개의 거리를 비교해서 최소값 갱신하는 방법. 마을 2개를 비교하는 것이기 때문에 2중 for문으로 해결 가능
for i in range(n):
  # d의 최대 값은 6000이다. (1000-(-1000) + ...)
  # 각 마을에서 가장 가까운 거리와 두번째로 가까운 거리를 저장할 변수
  min_a, min_b = 6000, 6000
  # 현재 마을 좌표
  x1,y1,z1 = arr[i]
  for j in range(n):
    # 같은 마을 스킵
    if i == j:
      continue
    x2,y2,z2 = arr[j] # 비교할 마을의 좌표
    d = abs(x1 - x2) + abs(y1 - y2) + abs(z1 - z2)

    # 현재 마을에서 가장 가까운 거리 갱신.
    if min_a > d:
      # 가장 가까운 거리가 갱신 되었으니 두번째로 가까운 거리는 원래 가장 가까웠던 마을의 거리
      min_b = min_a
      min_a = d
    else:
      # 새로 구한 거리가 두번째로 작은 거리보다 작은지 비교해서 갱신
      min_b = min(min_b, d)
  
  answer = min(answer, min_a + min_b)
print(answer)
