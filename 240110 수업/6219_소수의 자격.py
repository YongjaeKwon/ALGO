'''
A와 B 사이의 범위에서 'D'가 들어간 소수의 갯수 구하는 문제
1<= A<=B<=400만
1 <= A <= B <= A + 200만 <= 400만
B-200만 <= A <= 200만
A <= B <= A+ 200만
0 <= B-A <= A
0 <= B <= 2A
'''
import sys
input = sys.stdin.readline
A,B,D = map(int,input().split())

n = 4*(10**6)
is_Prime = [True for _ in range(n + 1)]
is_Prime[1] = False
for i in range(2,n+1):
  if not is_Prime[i]:
    continue
  for j in range(i*i, n+1, i):
    is_Prime[j] = False

cnt = 0
for a in range(A,B+1):
  if is_Prime[a] == True:
    if str(a).count(str(D)) > 0:
      cnt += 1

print(cnt)