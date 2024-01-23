'''
임의의 지점에서 시작, 원하는 지점에서 탈출, 산책한 구간 내에 있는 모든 조약돌 줍기
까만색 싫음 B이하개
하얀색 좋음 W이상개
만족하는 구간 없으면 집감
'''
import sys
input = sys.stdin.readline

N, b_cnt, w_cnt = map(int,input().split())
stone = input().rstrip()

dict = {'W': 0, 'B': 0}
max_length = 0

s, e = 0, 0
while e < N:
  if stone[e] == 'W':
    dict['W'] += 1
  else:
    dict['B'] += 1
  while dict['B'] > b_cnt:
    if stone[s] == 'W':
      dict['W'] -= 1
    else:
      dict['B'] -= 1
    s += 1
  # 하얀조약돌이 최소 기준 이상이면 answer 갱신
  if dict['W'] >= w_cnt:
    max_length = max(max_length,e - s + 1)
  e += 1
print(max_length)