'''
배열이 주어졌을 때 연속적인 K의 온도 중 가장 큰 온도 합.
1. 투포인터(슬라이딩 윈도우)
2. 구간 합을 계속해서 반복하기 때문에 누적합
'''
import sys
input = sys.stdin.readline

#1 투포인터 풀이
# n, k = map(int,input().split())

# s = 0
# e = k-1
# arr = list(map(int,input().split()))
# max_ = -1 * sys.maxsize
# sum_ = sum(arr[s:e+1])
# while e < n:
#   if sum_ > max_:
#     max_ = sum_
#   sum_ -= arr[s]
#   s +=1
#   e += 1
#   if e == n:
#     break
#   sum_ += arr[e]
# print(max_)

# 누적합 풀이
n, k = map(int,input().split())
arr = [0] + list(map(int,input().split()))
prefix = [0] * (n+1)
for i in range(1,n+1):
  prefix[i] = prefix[i-1] + arr[i]

max_ = -1 * sys.maxsize
for j in range(n-k+1):
  max_ = max(max_, (prefix[j+k] - prefix[j]))
print(max_)