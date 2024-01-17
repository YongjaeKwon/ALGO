'''
a,d
q 개수
쿼리
'''
import sys
input = sys.stdin.readline

def get_gcd(a,b):
    if b == 0:
        return a
    while a%b !=0:
        a, b = b, a%b
    return b

a, d = map(int,input().split())
Q = int(input())
for i in range(Q):
  q, l, r = map(int,input().split())
  # 쿼리가 1일때, 2일때 나눠서 푼다
  if q == 1:
    # 등차수열의 합을 구한다.
    # 공식을 이용
    # Sn = n(2a + (n-1)d)//2
    sum1 = (r * ((2 * a) + (r - 1) * d)) // 2
    sum2 = ((l - 1) * ((2 * a) + (l - 2) * d)) // 2
    answer = sum1 - sum2
  # 최대 공약수를 구한다.
  else:
    # 수가 한개일 경우 그 수가 최대 공약수
    if l == r:
      answer = a + d * (l-1)
    else:
    # 초항과 공차의 최대 공약수가 전체 수열의 공약수다.
      answer = get_gcd(a,d) 
  print(answer)