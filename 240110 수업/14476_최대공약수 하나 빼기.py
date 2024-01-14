'''
N = 최대 100만
'''
import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
arr = list(map(int,input().split()))

def get_gcd(a,b):
	if b == 0:
		return a
	while a%b != 0:
		a,b = b, a%b
	return b

arr = deque(arr)
max_GCD = 0
last_k = 0
answer = []
for i in range(N):
	K = arr.popleft()
	# 임의의 최소 공배수를 arr[0]번으로 둔다.
	GCD = arr[0]
	# 한개를 뺏으니 arr의 길이는 N-1
	for j in range(1,N-1):
		GCD = get_gcd(GCD,arr[j])
	# GCD가 K의 약수인지 판별
	if K%GCD == 0:
		arr.append(K)
		continue
	if max_GCD < GCD:
		max_GCD = GCD
		last_k = K
	arr.append(K)
if max_GCD == 0:
	print(-1)
else:
	print(max_GCD, last_k)
	