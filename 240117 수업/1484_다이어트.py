'''
G킬로그램을 쪘다.
현재 몸무게의 제곱에서 기억하고 있는 몸무게의 제곱을 뺀 것.

현재 몸무게 X
기억하고 있는 몸무게 Y
X**2 - Y**2 = G
현재 Y가 될수 있는 수를 구하여라~
1 <= G <= 100,000
x 최대 100000
y 최대 100000
'''
import sys
input = sys.stdin.readline

G = int(input())
x = 1
y = 1
ans = []
while x <= 100000 and y <= 100000:
  temp = x**2 - y**2
  if temp == G:
    ans.append(x)
    x += 1
  if temp > G:
    y += 1
  elif temp < G:
    x += 1

if len(ans) == 0:
  print(-1)
else:
  for i in ans:
    print(i)