'''
4중 for문으로 하면 600**4 => 129,600,000,000
시간 초과
3중 for문으로 줄이면 => 216,000,000
얼추 가능하다.
'''
import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int,input().split()))

arr.sort()
answer = 1000000000000000
for i in range(n):
	for j in range(n):
		if i == j:
			continue
		#arr[i] + arr[j]랑 가장 가까운 두 수를 찾고싶다.
		s = 0
		e = n-1
		while s < e:
			# 겹치면 안되기 때문에
			if s == i or s == j:
				s +=1
				continue
			if e == i or e == j:
				e -= 1
				continue

			answer = min(answer, abs(arr[i] + arr[j] - (arr[s] + arr[e])))
			if arr[s] + arr[e] > arr[i] + arr[j]:
				e -= 1
			else:
				s += 1

print(answer)