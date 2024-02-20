'''
숫자를 입력받고 상대방의 수가 내 숫자로 나누어 떨어지면 +1
상대방의 숫자로 내 숫자가 나누어 떨어지면 -1
아니면 무승부
n = 플레이어 수
본인을 제외한 모든 플레이어와 대결
같은 숫자는 등장하지 않는다.
n = 10만
=> 2중 for문 시간초과
'''
import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
set_arr = set(arr)
M = max(arr)
check = [0 for _ in range(M+1)]
for i in arr:
  # 2의 배수부터 최대 숫자까지의 배수 확인해서 check에 메모
  for j in range(2*i, M+1, i):
    # 조회에 시간이 오래 걸리기 때문에 set을 통해 조회 속도를 빠르게 한다.
    if j in set_arr:
        check[i] += 1
        check[j] -= 1
for i in arr:
  print(check[i], end = ' ')