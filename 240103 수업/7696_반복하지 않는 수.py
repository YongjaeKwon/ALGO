'''
같은 숫자를 두번 쓰는 것을 못하게 해보자
ex) 11, 22, 33
그리고 n이 0으로 입력되면 프로그램을 종료한다.
while문으로 전부 다 순회하면 돌렸을 때 100만이 입력되면 26195083
1. 문자열로 형 변환하면 시간 초과
2. 순열로 풀기
'''
import sys
input = sys.stdin.readline
from itertools import permutations
# 최대 값이 26195083 8자리
nums = [1,2,3,4,5,6,7,8,9]
arr = []
for i in range(1,9):
  a = list(permutations(nums,i))
  for j in range(len(a)):
    print(a[j][0])
  if i == 2:
    break




# while True:
#   n = int(input())
#   if n == 0:
#     break
#   print(arr[n])