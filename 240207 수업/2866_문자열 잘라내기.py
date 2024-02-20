'''
'''
import sys
from collections import defaultdict
input = sys.stdin.readline
r,c = map(int,input().split())
arr = [list(input().rstrip()) for _ in range(r)]
s,e = 0,r-1

answer = 0
while s<=e:
  mid = (s+e)//2
  duplicate = False
  dict = defaultdict(int)
  for j in range(c):
    temp = ''
    # 행을 이분 탐색하며 중복을 확인한다. (r행까지 끝까지 확인함)
    for i in range(mid,r):
      temp += arr[i][j]
    # 중복 되었는지 체크
    if dict[temp]:
      duplicate = True
      break
    else:
      dict[temp] += 1
  # 중복이 확인 되었으면 더 작은 높이를 찾아야함
  if duplicate:
    e = mid - 1
  # 중복이 없다면 더 큰 높이를 시도해봐야함
  else:
    answer = mid
    s = mid + 1
print(answer)