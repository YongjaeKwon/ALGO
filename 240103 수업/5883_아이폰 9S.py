'''
줄을 지어서 있을때, 특정 용량을 원하는 고객을 따로 뽑아서 줄에서 빼버렸을 때, 연속되는 길이가 가장 긴 연속된 길이 구하기
일단 용량의 1~1,000,000까지 전부 제거해본다. => 최대 1000 * 1,000,000의 연산 (시간 초과)
=> 줄일 수 있는 용량 크기를 조절: 용량의 종류를 걸러내서 해본다.
'''
import sys
input = sys.stdin.readline
from copy import deepcopy

N = int(input())
line = []
for i in range(N):
  line.append(int(input()))

type_B = list(set(line))
# 정답 갱신할 변수 (최소값은 항상 1)
answer = 0
for i in type_B:
  temp_line = deepcopy(line)
  cnt = 0
  # 용량을 한개씩 전부 list에서 제거해본다
  while i in temp_line:
    temp_line.remove(i)
  # 한칸씩 진행해 보면서 최대 길이를 구한다.
  for i in range(len(temp_line)-1):
    if temp_line[i] == temp_line[i+1]:
      cnt += 1
    else:
      answer = max(answer,cnt)
      cnt = 0
    # 맨 마지막줄까지 포함해야할 경우를 고려하여 한번더 max실행
    answer = max(answer, cnt)
print(answer+1)
