'''
정렬되어있는 배열 A,B
두 배열을 합친 다음 정렬해서 출력
'''
import sys
input = sys.stdin.readline

n,m = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

'''
C = A+B
C.sort()
for i in C:
  print(i, end=' ')

통과가 되긴 하지만 우리는 투포인터로 해결해본다.  
'''
a = 0
b = 0

while True:
  if a == n and b == m:
    break
  if a == n and b != m:
    while b < m:
      print(B[b], end=' ')
      b += 1
    break
  if a != n and b == m:
    while a < n:
      print(A[a], end=' ')
      a += 1
    break
  if A[a] > B[b]:
    print(B[b], end=' ')
    b += 1
  elif A[a] == B[b]:
    print(A[a], end=' ')
    print(B[b], end=' ')
    a += 1
    b += 1
  else:
    print(A[a], end= ' ')
    a += 1