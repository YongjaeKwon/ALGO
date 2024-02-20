'''
원소 하나를 뺐을때 정렬되어있는 배열을 남길 수 있는 경우의 수.
9
1 1 3 4 5 8 9 10 0
'''
import sys
input = sys.stdin.readline

N = int(input())
arr = [-10**9 - 1] + list(map(int, input().split())) + [10**9 + 1]

ans = 0
cnt = 0
before_dec = 0
after_dec = 0

# 배열을 순회하며 감소하는 부분 수와 해당 부분의 시작과 끝 인덱스를 찾음
for i in range(1, N + 1):
    # 현재 원소가 이전 원소보다 작으면 (감소하는 부분을 찾았을 때)
    if arr[i] < arr[i - 1]:
        cnt += 1
        before_dec = i - 1 # 감소하는 부분의 시작 인덱스 기록
        after_dec = before_dec + 1 # 감소하는 부분의 끝 인덱스 기록

# 경우의 수 계산
if cnt == 0:
    ans = N  # 모든 원소가 증가하는 경우
elif cnt > 1:
    ans = 0  # 두 번 이상 감소하는 부분이 있으면 정렬이 불가능
else:
    # 선택한 부분의 왼쪽과 오른쪽 값이 정렬된 배열이 되도록 할 수 있는지 확인
    if arr[before_dec - 1] <= arr[after_dec]:
        ans += 1
    if arr[before_dec] <= arr[after_dec + 1]:
        ans += 1

print(ans)
