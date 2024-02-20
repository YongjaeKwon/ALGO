'''

'''
import sys
from collections import defaultdict
input = sys.stdin.readline
n,k = map(int,input().split())
arr = [0] + list(map(int,input().split()))
prefix = [0] * (n+1)

for i in range(1,n+1):
  prefix[i] = prefix[i-1] + arr[i]

dict = defaultdict(int)

cnt = 0
for i in range(1,n+1):
  if prefix[i] == k:
    cnt += 1
  # prefix[i]-k 가 dict에 있다면 그 수만큼 cnt에 추가
  if prefix[i]-k in dict:
    cnt += dict[prefix[i]-k]
  dict[prefix[i]] += 1
print(cnt)