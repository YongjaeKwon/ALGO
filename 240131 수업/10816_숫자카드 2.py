'''
각 숫자를 상근이가 몇개 가지고 있는지.
갯수를 빠르게 조회하기 위해 먼저 dict를 생성.
'''
import sys
input = sys.stdin.readline
from collections import defaultdict

n = int(input())
arr1 = list(map(int,input().split()))
m = int(input())
arr2 = list(map(int,input().split()))

arr1.sort()
dict = defaultdict(int)

for i in arr1:
  dict[i] += 1

for j in arr2:
  if j in dict:
    print(dict[j], end=' ')
  else:
    print(0, end= ' ')


    