'''
S의 모든 소인수가 10^6 보다 큰 소수 인지 판별하는 문제
그러면 소인수를 구하는 코드를 짜고, 그 다음에 모든 소인수가 10^6 보다 큰지 판별
소인수 = 1을 제외한 나눌 수 있는 모든 수.
2부터 S가 될때까지 나눠보면 된다.
=> 시간 초과

# 그렇다면 10^6 까지 전부 나눠보면서 나누어 떨어진다면 NO를 출력
'''
import sys
input = sys.stdin.readline



N = int(input())
for _ in range(N):
  answer = 'YES'
  S = int(input())
  for i in range(2,10**6+1):
    if S % i == 0:
      answer = "NO"
      break
  print(answer)
