'''
용사 진수가 K명의 병사를 이기려면 최소 스탯의 합은?
N은 최대 100
K도 최대 100
'''
import sys
input = sys.stdin.readline

N, K = map(int,input().split())
soldier = []
for i in range(N):
  strength, agility, intellect = map(int,input().split())
  soldier.append([strength, agility, intellect])

cnt = 0
for i in soldier:
  strength, agility, intellect = i

# 총 능력치의 최소 값을 구할 것. (기본값 최대)
min_stats = sys.maxsize
# 모든 병사들의 각 개별 스탯을 탐색하면서 K명을 이길 수 있는 상태를 만들 것.
for i in range(N):
    for j in range(N):
        for k in range(N):
            # 이길수 있는 병사의 수를 셀 cnt 변수
            cnt = 0
            for n in range(N):
                if (soldier[i][0] >= soldier[n][0] and soldier[j][1] >= soldier[n][1] and soldier[k][2] >= soldier[n][2]):
                    cnt += 1
                    # 이길 수 있는 병사의 수가 K에 도달 했을때, 기존의 능력치 최소값과 비교하여 갱신.
                    if cnt == K:
                        min_stats = min(min_stats, soldier[i][0] + soldier[j][1] + soldier[k][2])
                        break

print(min_stats)