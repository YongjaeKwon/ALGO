import sys
input = sys.stdin.readline

def recur(cur, total):
  if cur == n:
    ans = max(ans, )
    return
  
  recur(cur+1, total)
  recur(cur+1, total + 1)

n = int(input())
arr = list(map(int,input().split()))

