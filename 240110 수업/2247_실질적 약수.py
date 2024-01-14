'''
SOD를 구현
CSOD를 구현
그 후 1,000,000으로 나눈 나머지 출력
1. 약수를 모두 더하기 했더니 시간 초과.
=> n이 소수인 아이들은 전부 0

'''
import sys
input = sys.stdin.readline

n = int(input())
# 자기와 자신을 제외한 약수를 모두 더한 값.
def SOD(n):
  answer = 0
  for i in range(2,n+1):
    if i * i > n:
      break
    if n%i == 0:
      answer += i
      if i * i != n:
        answer += n//i
  return answer


def CSOD(n):
  answer = 0
  for i in range(1,n+1):
    answer += SOD(i)
  return answer

print(CSOD(n) % 1_000_000)

print(SOD(n))