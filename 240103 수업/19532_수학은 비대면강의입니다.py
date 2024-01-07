'''
-999 <= x , y <= 999
x,y의 해가 유일하게 존재
'''
import sys
input = sys.stdin.readline

a,b,c,d,e,f = map(int,input().split())

for x in range(-999,1000):
  for y in range(-999,1000):
    if a*x + b*y == c and d*x + e*y == f:
      print(x, y)
      break