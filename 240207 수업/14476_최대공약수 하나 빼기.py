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
for i in range(n-1,0,-1):
  suffix[i] = get_gcd(suffix[i+1],arr[i])

answer = []
# prefix와 suffix를 통해 i를 제외한 모든 최대 공약수를 배열안에 담을 수 있다.
for i in range(1,n):
	gcd = get_gcd(prefix[i-1],suffix[i+1])
	if arr[i]%gcd == 0:
		continue
	# gcd와 뺀 수를 넣어준다.
	answer.append([gcd,arr[i]])

if answer:
	print(answer[-1][0],answer[-1][1])
else:
	print(-1)