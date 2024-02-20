'''
WHEE 완성하는 문제.
H를 먼저 찾고 앞 뒤의 문자열들을 찾아주면 된다.
'''
import sys
input = sys.stdin.readline

n = int(input())
S = input().rstrip()

prefix = [0] * n
suffix = [0] * n

w_cnt = 0
for i in range(n):
  if S[i] == 'W':
    w_cnt += 1
  prefix[i] = w_cnt

e_cnt = 0
for i in range(n-1,-1,-1):
  if S[i] == 'E':
    e_cnt += 1
  suffix[i] = e_cnt

answer = 0
for i in range(n):
  if S[i] == 'H':
    answer += prefix[i] * (2**(suffix[i]) - 1 - suffix[i])
modular = 10**9+7
print(answer%modular)