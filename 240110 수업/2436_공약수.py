'''
A,B가 주어졌을 때, 
A가 최대 공약수
B가 최소 공배수인 두개의 자연수를 구하여라
여러쌍이 나올 경우 A+B가 가장 작은 것이 정답.
'''
import sys
input = sys.stdin.readline

# A: 최대 공약수 / B: 최소 공배수
g,l = map(int,input().split())

# 최소공배수를 최대공약수로 나누면 나머지가 나옴
leftover = l // g

def get_gcd(a,b):
  if b == 0:
    return a
  while a%b != 0:
    a, b = b, a%b
  return b


# 나머지중에서 제곱근까지 돌면서 (제곱근에 가까울수록 차이가 적다.)
for x in range(int(leftover**0.5),0,-1):
  y = int(leftover/x)
  # 만약 x가 나머지의 소인수이고. / y와의 최대공약수가 1이라면 (서로소)
  if leftover%x == 0 and get_gcd(x,y) == 1:
    print(x*g,y*g)
    break
