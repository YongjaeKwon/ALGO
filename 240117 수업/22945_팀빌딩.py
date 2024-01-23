'''
하나의 팀에는 최소 2명
(A와B 사이에 존재하는 다른 개발자 수) * min(A능력치,B능력치)
1 2 3 4
0 1 2 3
3 - 0 -1 =2 
(e - s - 1)
'''
import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int,input().split()))
answer = 0
s, e = 0, N-1

while s < e:
  answer = max(answer, (e - s - 1) * min(arr[s], arr[e]))
  # 최대 값을 구하고 싶은 것이기 때문에 최소값을 갱신해가면서 포인터 이동
  if arr[s] < arr[e]:
    s += 1
  else:
    e -= 1
print(answer)