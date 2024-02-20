'''
누적합이 아닌 누적 GCD를 구한다.

'''
import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
arr = [0] + list(map(int,input().split()))

def get_gcd(a,b):
	if b == 0:
		return a
	while a%b != 0:
		a,b = b, a%b
	return b

prefix = [0 for _ in range(n+1)]
suffix = [0 for _ in range(n+1)]

prefix[1] = arr[1]
suffix[n] = arr[n]
for i in range(2,n+1):
	prefix[i] = get_gcd(prefix[i-1],arr[i])
for j in range(n-1,0,-1):
	suffix[j] = get_gcd(suffix[j+1], arr[j])

# 해당 숫자의 좌 우 gcd들의 gcd가 i를 제외한 최대 공약수.
answer = []
for i in range(1,n):
	gcd = get_gcd(prefix[i-1],suffix[i+1])
	if arr[i] % gcd == 0:
		continue
	answer.append((gcd,arr[i]))

answer.sort()
print(answer[-1][0],answer[-1][1]) if answer else print(-1)