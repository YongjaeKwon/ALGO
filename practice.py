'''
6
1 8 2 3 6 10
9
1 1
2 2
3 3
1 2
1 3
1 7
7 1
3 1
2 1
'''
import sys
input = sys.stdin.readline

N = int(input())
barn = list(map(int,input().split()))
Q = int(input())

barn.sort()

def min_cost(a,b,x,y):
  answer = 0
  if y >= x:
    answer += a*(y-x)
  else:
    answer += b*(x-y)
  return answer

for _ in range(Q):
  answer = sys.maxsize
  a,b = map(int,input().split())
  for i in range(N):
    y = barn[i]
    temp = 0
    for j in range(N):
      x = barn[j]
      temp += min_cost(a,b,x,y)
    answer = min(temp, answer)
  print(answer)