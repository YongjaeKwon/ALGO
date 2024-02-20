'''
상근이가 가지고 있는 수자 카드의 개수 N
M 개의 카드 중에서 상근이가 가지고있는지 없는지 구해야할 카드
'''
import sys
input = sys.stdin.readline

n = int(input())
arr1 = list(map(int,input().split()))
m = int(input())
arr2 = list(map(int,input().split()))
# 이진 탐색을 위해 arr2 정렬
arr1.sort()

for i in range(m):
  target = arr2[i]
  s = 0
  e = n-1
  flag = False
  while s <= e:
    mid = (s+e)//2
    if target < arr1[mid]:
      e = mid - 1
    elif target > arr1[mid]:
      s = mid + 1
    else:
      flag = True
      break
  if flag == True:
    print(1, end= ' ')
  else:
    print(0, end= ' ')