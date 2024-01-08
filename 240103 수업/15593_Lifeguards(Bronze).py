'''
1 <= N <= 100
N명의 인원중에서 1명을 해고해야 할 때, 최대 커버할 수 있는 시간을 구하는 문제.
4시에 시작해서 7시에 끝나는 사람은 3시간을 커버할 수 있음
따라서 한명이 일을 하는 시간은 end - start
'''
import sys
input = sys.stdin.readline
from copy import deepcopy

N = int(input())
time = []
# 각 cow의 근무 시간
cow = []
for _ in range(N):
  temp = []
  start, end = map(int,input().split())
  for i in range(start,end):
    time.append(i)
    temp.append(i)
  cow.append(temp)

max_time = 0
# time을 복사해서 cow에서 하나씩 꺼낸 다음 해당 근무 시간을 다 빼보면서 비교해본다.
for i in range(len(cow)):
  temp_time = deepcopy(time)
  for j in range(len(cow[i])):
    temp_time.remove(cow[i][j])
  work_time = len(list(set(temp_time)))
  max_time = max(max_time, work_time)

print(max_time)


  