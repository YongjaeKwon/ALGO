'''
신호등 고치기
고장난 신호등을 X로 바꾼 후, s,e 를 K간격 만큼 잡아둔 후, e를 N+1까지 돌려서 최소 X의 갯수를 cnt.
.count() 를 While문 안에 넣으면 매번 연산횟수가 소모가 된다.
=> arr[s]와 arr[e]의 값만 보고 cnt를 빼고 더해서 최소값을 계산하는 것이 연산 속도가 훨신 짧다.
'''
import sys
input = sys.stdin.readline

N, K, B = map(int,input().split())
arr = [i for i in range(N+1)]
for _ in range(B):
  arr[int(input())] = 'X'

# 최대 10만개 고장날 수 있음.
cnt = 100000
s = 1
e = K
temp = arr[s:e+1].count('X')

while e < N:
  if arr[s] == 'X':
    temp -= 1
  s += 1
  e += 1
  if arr[e] == 'X':
    temp += 1
  cnt = min(temp,cnt)

print(cnt)