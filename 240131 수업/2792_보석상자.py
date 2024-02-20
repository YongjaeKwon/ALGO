'''
m가지의 서로다른 색상
학생은 한가지의 색상만 가져간다.
질투심 = 가장 보석을 많이 가져간 학생이 가진 보석 수.
n명의 학생에게 보석을 나누어 주었을때 최소가 되는 질투심 수치를 구하라
ex RR RR BB BB BBB
=> 3


'''
import sys
input = sys.stdin.readline

n,m = map(int,input().split())
arr = []
for _ in range(m):
  arr.append(int(input()))
arr.sort()
#최소 보석 수 1
s = 1
#최대 보석 수
e = arr[-1]

while s <= e:
  mid = (s+e)//2
  total = 0
  for i in arr:
    