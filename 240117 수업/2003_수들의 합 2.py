import sys
input = sys.stdin.readline

n,m = map(int,input().split())
arr = list(map(int,input().split()))

s = 0
e = 0
total = arr[0]
cnt = 0
while True:
  if total < m:
    if e < n:
      e += 1
      total += arr[e]
    else:
      break
  elif total > m:
    total -= arr[s]
    s += 1
  elif total == m:
    cnt += 1
    total -= arr[s]
    s += 1

print(cnt)