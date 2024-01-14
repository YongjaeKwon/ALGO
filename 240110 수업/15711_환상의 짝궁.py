'''
골드바흐의 추측:
2보다 큰 모든 짝수는 두 소수의 합으로 표현이 가능하다.
홀수를 처리해주면 될듯 싶다.
홀수는 소수 + 소수 ?
=> 한쪽이 짝수여야 함.
=> 짝수인 소수는 2밖에 없음
=> 2 + B = 소수
(예외 처리 먼저: A + B의 합이 1, 2, 3은 항상 "NO")
B를 소수 판별
B의 범위는 2*10**12까지
T가 주어지고 그 밑에 T의 개수만큼 A,B가 주어지는 문제이다.
각 Testcase 별로 소수 판정을 한다면? (시간초과가 날 것 같지만 시도해본다.)
=> 시간 초과.
=> 에라토스테네스의 채로 소수인지를 판별할 수 있도록 미리 is_Prime 을 만들어 각 Testcase마다 판단.
B의 최대 크기인 2*(10**12) 까지 구하면 (메모리 초과)
=> 최적화가 필요하다.
=> 루트 4*10**12 까지의 소수를 구해서
=> A+B가 2*10**6 보다 크다면 (A+B) -2 가 소수로 나누어지는지를 확인한다.
=> 소수로 나누어 진다면 소수가 아니다. 안나누어지면 소수다.
=> A+B가 2*10**6 보다 작다면 (A+B) -2 가 소수인지를 확인한다. 
'''
import sys
input = sys.stdin.readline

n = (4*(10**12))**(0.5)
is_Prime = [True for i in range(int(n)+1)]
is_Prime[1] = False
for i in range(2,int(n)+1):
  if not is_Prime[i]:
    continue
  for j in range(i*i, int(n)+1, i):
    is_Prime[j] = False

# 나누어줄 소수 모음을 구한다.
sosu = []
for index in range(2,len(is_Prime)):
  if is_Prime[index] == True:
    sosu.append(index)

T = int(input())

for i in range(T):
  A,B = map(int,input().split())
  # 예외처리 먼저
  if A + B <= 3:
    print("NO")
    continue
  # 짝수일 경우 (골드바흐의 추측)
  if (A+B)%2 == 0:
    print("YES")
    continue
  # 홀수일 경우 (B를 소수 판별하면 된다? => (A+B) -2 가 소수이면 된다)
  answer = "YES"
  if (A+B) > 2*(10**6):
    for i in sosu:
      if ((A+B)-2) % i == 0:
        answer = "NO"
        # 나누어지는 수를 찾았다면 BREAK
        break
  else:
    if (A+B) - 2 in sosu:
      answer = "YES"
    else:
      answer = "NO"
  print(answer)