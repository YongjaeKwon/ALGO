'''
'''
import sys
input = sys.stdin.readline
n = int(input())
arr= list(map(int,input().split()))
target = int(input())

s = 0
e = n-1
# 두수의 합을 고르기 위해서 정렬을 한다
arr.sort()

cnt = 0
# 시작과 끝 지점을 설정하여 후보군을 하나씩 줄여가면서 탐색
while s < e:
  # 더한 값이 크다면 e 기준에서 어떤 수를 더해도 target보다 큰 값이 나오므로 더이상 볼 필요가 없다.
  if arr[s] + arr[e] > target:
    e -= 1
  # 더한 값이 target보다 작다면 s보다 작은 값들은 볼 필요가 없으므로 s += 1
  elif arr[s] + arr[e] < target:
    s += 1
  # 정렬된 상태에서 (중복된 값이 없기 때문에) s의 후보군을 줄이든, e의 후보군을 줄이든 한가지만 줄이면 된다.
  elif arr[s] + arr[e] == target:
    cnt += 1
    s += 1
    # e -= 1
print(cnt)