'''
개똥벌레가 뚫어야 하는 벽의 최소 값과 최소값의 갯수.
홀수번째는 앞에서 부터 업데이트
짝수번째는 뒤에서부터 업데이트
IMOS문제
=> 모든 업데이트를 진행한 후에 누적합을 구한다.
'''
import sys
input = sys.stdin.readline
n, h = map(int, input().split())

prefix = [0] * h

for i in range(n):
    wall = int(input())
    if i % 2 == 0:
        # 석순의 경우: 높이에 따라 배열 업데이트
        prefix[h - wall] += 1
    else:
        # 종유석의 경우: 높이 0에서 배열 업데이트, 그리고 해당 높이에서 종유석 파괴 (-1)
        prefix[0] += 1
        prefix[wall] -= 1

# 누적 합 계산
for i in range(1, h):
    prefix[i] += prefix[i - 1]

min_value = min(prefix)
min_count = prefix.count(min_value)

print(min_value, min_count)
