'''
'''
import sys
input = sys.stdin.readline

n,k = map(int,input().split())
arr = []
for _ in range(n):
  arr.append(int(input()))

s = 1
# 최대값을 끝 지점으로
e = max(arr)

while s <= e:
  people = 0
  mid = (s+e)//2
  
  # mid로 i값들을 나눈 만큼 더하면 K명에게 나누어 줄 수 있는지 판별 가능.
  for i in arr:
    people += (i//mid)
  # k명 이상에게 나누어줄 수 있다면. mid 값이 나누어줄 수 있는 수.
  # print('mid',mid)
  # print('people',people)
  if people >= k:
    answer = mid
    s = mid + 1
  # k명에게 모두 못나누어줄 경우 e값을 mid -1로 조정.
  else:
    e = mid - 1
print(answer)