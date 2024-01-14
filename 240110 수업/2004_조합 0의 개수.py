'''
nCm에서 0의 갯수를 출력하라.
nCm = n! / ((n-m)! * m!)
n과 m은 20억까지 가능........
10을 곱했을 때 뒷자리에 0이 하나씩 추가 되므로
2*5의 식으로 나타냈을때
n!에서의 2와 5의 지수를 구하고 여기서
(n-m)!의 2와 5의 지수를 구하고 뺸다
m!의 2와 5의 지수를 구해서 뺀다.
강의에서 7번에 n!에 곱해져있는 소수 k의 개수를 활용하여 구해본다. => (logN) 까지 줄어들음
'''
import sys
input = sys.stdin.readline

# 교수님이 구현해 보라고 하신 방법!
def get_k_cnt(N,K):
	cnt = 0
	init_K = K
	while K <= N:
		cnt += N//K
		K *= init_K
	return cnt

n,m = map(int,input().split())

# N!에서 2,5의 갯수 구하기
N_2, N_5 = get_k_cnt(n,2), get_k_cnt(n,5)
N_M_2, N_M_5 = get_k_cnt(n-m,2), get_k_cnt(n-m,5)
M_2, M_5 = get_k_cnt(m,2),get_k_cnt(m,5)

# 10의 갯수를 구하기 위해서는 2와 5의 10의 최소값을 찾으면 된다!
answer = min(N_2 - N_M_2 - M_2, N_5 - N_M_5 - M_5)
print(answer)