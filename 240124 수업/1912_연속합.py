'''
10
10 -4 3 1 5 6 -35 12 21 -1
연속된 부분수열 중에서 합이 가장 큰 숫자를 구한다.
'''
import sys
input = sys.stdin.readline

n = int(input())
arr = [0] + list(map(int,input().split()))
prefix = [0] * (n+1)

for i in range(1,n+1):
  # 이전까지의 합과 현재 값을 비교해서 최대값을 누적한다.
  prefix[i] = max(arr[i],prefix[i-1] + arr[i])
prefix.pop(0)
print(max(prefix))