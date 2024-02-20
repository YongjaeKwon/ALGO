'''
MBTI의 글자가 다르면 거리 +1 같으면 0
가장 가까운 3명의 MBTI
완전탐색 시작
시간제한 2초 = 2억번 연산
N = 10만
10만C2 =>10만 * 99999 / 2
=> 5만 * 10만 => 50억 (시간초과)
총 MBTI의 갯수는 16개 안겹치게 2명씩 있어도 최대 32개
=> 따라서 N이 32보다 크면 무조건 겹치는 3개가 발생하게됨.
=> 이때 답은 무조건 0을 출력한다. 그러면 우리는 32개의 조합 안에서만 놀면 된다.
=> 3중 for문 32 * 32 * 32 => 매우 넉넉하게 가능.
'''

import sys
input = sys.stdin.readline

T = int(input())
for i in range(T):
  n = int(input())
  arr = list(input().split())
  if n > 32:
    print(0)
    continue
  else:
    # 3개를 고르려면 3중 for문
    answer = sys.maxsize
    for i in range(n):
      for j in range(n):
        for k in range(n):
          # 겹치는 index가 없어야한다.
          score = 0
          if i == j or i == k or j == k:
            continue
          else:
            for index in range(4):
              if arr[i][index] != arr[j][index]:
                score += 1
              if arr[i][index] != arr[k][index]:
                score += 1
              if arr[j][index] != arr[k][index]:
                score += 1
            answer = min(answer,score)
    print(answer)
  