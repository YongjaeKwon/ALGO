'''
'''
import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int,input().split()))
answer = 0
s, e = 0, N-1

# 같은 팀원을 고르면 안되기 때문에 s<e
while s < e:
  answer = max(answer, (e - s - 1) * min(arr[s], arr[e]))
  # 더 작은값을 이동해준다.
  if arr[s] < arr[e]:
    s += 1
  else:
    e -= 1
print(answer)