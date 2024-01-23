'''
난쟁이 투포인터로 풀기
7명의 난쟁이가 있었는데 9명이 되어버렸다.
7명의 키의 합이 100이였다.
일곱 난쟁이를 찾는 프로그램을 작성하라.
'''
import sys
input = sys.stdin.readline
arr = []
for _ in range(9):
  arr.append(int(input()))

#투포인터 적용을 위해 arr 정렬하기
arr.sort()
s = 0
e = 8
height = sum(arr) - 100
while s<=e:
  temp = arr[s] + arr[e]
  if temp > height:
    e -= 1
  elif temp == height:
    for i in range(9):
      if i != s and i!=e:
        print(arr[i])
    break
  else:
    s +=1