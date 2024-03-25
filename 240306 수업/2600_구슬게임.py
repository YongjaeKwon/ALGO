import sys
input = sys.stdin.readline

b1,b2,b3 = map(int,input().split())

for i in range(5):
  k1, k2 = map(int,input().split())


def recur(cur, cnt, k1, k2):

  if cur == n:
    ans = min(ans, cnt)
    return
  

  recur(cur+1, k1 - b1, k2)
  recur(cur+1, k1 - b2, k2)
  recur(cur+1, k1 - b3, k2)
  recur(cur+1, k1, k2 - b1)
  recur(cur+1, k1, k2 - b2)
  recur(cur+1, k1, k2 - b3)
