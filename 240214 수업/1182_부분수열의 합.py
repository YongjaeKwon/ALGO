'''
부분수열: 연속하지 않아도 됨...
'''
import sys
input = sys.stdin.readline

n, s = map(int,input().split())
arr = list(map(int,input().split()))
cnt = 0
def recur(cur,sum_):
  global cnt
  if cur == n:
    return
  sum_ += arr[cur]
  if sum_ == s:
    cnt += 1
  # 해당 index의 값을 더해준 거
  recur(cur+1, sum_)
  # 해당 index의 값을 스킵한 거
  recur(cur+1, sum_ - arr[cur])

recur(0,0)
print(cnt)