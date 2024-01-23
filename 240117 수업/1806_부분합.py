'''
수열의 부분 합 중 S 이상이 되는것 중에서 가장 짧은 길이를 구하는 프로그램
'''
import sys
input = sys.stdin.readline
N, S = map(int,input().split())
arr = list(map(int,input().split()))

s = 0
e = 0
min_length = sys.maxsize
temp = arr[0]
while s <= e and e < N:
  if temp < S:
    e += 1
    if e == N:
      break
    temp += arr[e]
  else:
    min_length = min(min_length, e - s + 1)
    temp -= arr[s]
    s += 1
if min_length == sys.maxsize:
  print(0)
else:
  print(min_length)