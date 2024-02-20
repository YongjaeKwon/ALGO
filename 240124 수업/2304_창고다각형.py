'''
누적합 이용해서 풀어보기
'''
import sys
input = sys.stdin.readline

n = int(input())
arr = [0 for _ in range(1010)]
for i in range(n):
  a,b = map(int,input().split())
  arr[a] = b

prefix = [0 for _ in range(1010)]
prefix[0] = arr[0]
for i in range(1,1010):
  prefix[i] = max(prefix[i-1],arr[i])


suffix = [0 for _ in range(1010)]
suffix[0] = arr[0]
for i in range(1009)[::-1]:
  suffix[i] = max(suffix[i+1],arr[i])

answer = 0
for i in range(1010):
  answer += min(prefix[i],suffix[i])
print(answer)