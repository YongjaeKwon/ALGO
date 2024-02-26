import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
lst = list(map(int,input().split()))

if n == 100:
  print(0)
  exit()

def recur(cur, cnt):
  if cur == n:
    return
  
  recur(cur+1, cnt+1)

recur(0,100)
  