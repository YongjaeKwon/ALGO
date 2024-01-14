'''
0<= x <=N
0<= y <=M
점의 개수가 K개인 선분의 개수

모든 좌표의 시작과 끝 지점
유클리드 호제법을 사용하면, 시작점을 제외한 점의 갯수를 구할 수 있다.
따라서 x와 y의 범위가 가능한 두점에 대하여 모든 gcd를 + 1을 구하면 k개의 점을 포함하고 있는 선분의 갯수를 구할 수 있다. (시작점을 제외하고 점의 갯수가 세지기 때문에)
'''
import sys
input = sys.stdin.readline
# 유클리드 호제법
def get_gcd(a,b):
	if b == 0:
		return a
	while a%b != 0:
		a,b = b, a%b
	return b

N,M,K = map(int,input().split())

cnt = 0
for x in range(N+1):
	for i in range(N+1):
		for y in range(M+1):
			for j in range(M+1):
				if get_gcd(abs(i-x), abs(j-y)) + 1 == K:
					cnt += 1

# (0,0) (2,2) 와 (2,2) (0,0) 은 서로 같은 계산이기 때문에 cnt 1/2를 해주어야한다.
print(cnt//2)
