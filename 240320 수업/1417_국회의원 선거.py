import sys
input = sys.stdin.readline

n = int(input())
vote = int(input())
arr = list(int(input()) for _ in range(n-1))

arr.sort(reverse = True)

cnt = 0

if n == 1:
  print(cnt)
  exit()

while True:
  if arr[0] >= vote:
    arr[0] -= 1
    vote += 1
    cnt += 1

    arr.sort(reverse = True)

  else:
    break

print(cnt)