'''
A와 B를 더해서 7로 나누어 떨어지면 제거
=> 모듈러 연산을 통해 모든 수를 A%7로 바꾼다.
'''
import sys
input = sys.stdin.readline

N,M = map(int,input().split())
arr_A = list(map(int,input().split()))
arr_B = list(map(int,input().split()))

# arr_A를 전부 7로 나눈다.
for i in range(len(arr_A)):
  arr_A[i] = arr_A[i]%7
for j in range(len(arr_B)):
  arr_B[i] = arr_B[i]%7

for k in range(len(arr_A)):
  arr_A[i] += (arr_A[i] + arr_B[i]) % 7