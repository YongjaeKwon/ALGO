'''
숫자 야구
우리가 모르는 숫자 세자리 ***
숫자가 세개 주어짐

질문 횟수 = N
숫자가 맞는다 => Ball or Strike
숫자와 위치가 맞는다 => Strike
전체 숫자조합에서 불가능한 경우의 수를 줄이며 후보를 찾아낸다.
후보를 찾아 냈으면 다시 for문을 돌릴 때, 전체 숫자 조합에서 다시 찾는 것이 아니라, 추려낸 후보 내에서 찾아보면 필터링이 점점 되어서 최종 가능한 숫자들이 나온다.
'''
import sys
input = sys.stdin.readline

# 1~9로만 이루어진 숫자 3개로 전체 배열 만들기
baseball_list = []
for i in range(111,1000):
  baseball = str(i)
  if baseball[0]!='0' and baseball[1] !='0' and baseball[2] !='0':
    if baseball[0]!=baseball[1] and baseball[1]!=baseball[2] and baseball[0] != baseball[2]:
        baseball_list.append(baseball)
# 가능한 후보들을 모을 list
candidate = []
N = int(input())
for _ in range(N):
  predict, strike, ball = map(int, input().split())
  predict = str(predict)
  for baseball in baseball_list:
    temp_s = 0
    temp_b = 0
    for i in range(3):
      for j in range(3):
        # 값이 똑같고
        if predict[i] == baseball[j]:
          # 위치까지 똑같다면 strike
          if i == j:
            temp_s += 1
          # 아니라면 ball
          else:
            temp_b += 1

    if temp_s == strike and temp_b == ball:
      candidate.append(baseball)
  # 가능한 정답만을 추려가며 baseball_list를 갱신
  baseball_list = candidate
  # 다시 후보 초기화
  candidate = []
# 마지막으로 후보의 갯수 출력
print(len(baseball_list))



