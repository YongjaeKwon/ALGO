import sys
input = sys.stdin.readline

n = int(input())
arr = []
for i in range(n):
  x, y = map(int,input().split())
  arr.append((x,y))

# 끝난시간 기준으로 정렬 최대한 많은 수강실을 예약해야하기 때문에.
# 그 이후 시작 순서대로 정렬
arr.sort(key = lambda x: (x[1], x[0]))

available = 0
answer = []
for i in range(n):
  s, e = arr[i]
  if available <= s:
    answer.append(arr[i])
    available = e

print(len(answer))