'''
일렬로 버섯이 10개 있음.
순서대로 집을 수 있는데 한번 끊으면 뒤에 버섯은 모두 먹을 수 없음.
만약 100에 가까운 수가 2개라면 더 큰값을 선택한다.
'''
import sys
input = sys.stdin.readline

mushroom = []
for i in range(10):
  score = int(input())
  mushroom.append(score)

score = 0
temp = 0
for i in mushroom:
  temp = score
  score += i
  # 100이 넘어간다면
  if score >= 100:
    # 방금 더한것 까지와 / 이전까지 합해놓은 것을 비교해서 정답을 선택
    if score - 100 > 100 - temp:
      score = temp
      break
print(score)
