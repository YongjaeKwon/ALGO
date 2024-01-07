'''
1 <= N <= 100
N명의 인원중에서 1명을 해고해야 할 때, 최대 커버할 수 있는 시간을 구하는 문제.
4시에 시작해서 7시에 끝나는 사람은 3시간을 커버할 수 있음
따라서 한명이 일을 하는 시간은 end - start
'''
import sys
from copy import deepcopy
input = sys.stdin.readline

N = int(input())

time = {}
lifeguard = []
for _ in range(N):
  start, end = map(int,input().split())
  temp = []
  # 전체 커버 가능 시간을 append
  for i in range(start,end):
    if i in time:
      time[i] +=1
    else:
      time[i] = 1 
    # 각 lifeguard의 근무 시간을 append
    temp.append(i)
  lifeguard.append(temp)

max_time = 0

# 각각 빠졌을 때 커버 가능한 시간을 계산
for i in range(len(lifeguard)):
  # 얕은 복사 때문에 deepcopy 사용
  temp = deepcopy(time)
  for j in range(len(lifeguard[i])):
    temp[lifeguard[i][j]] -= 1
  cnt = 0
  # 근무 가능한 시간이 0 이상이면 커버 가능한 시간.
  for i in temp:
    if temp[i] > 0:
      cnt += 1
  max_time = max(max_time, cnt)
