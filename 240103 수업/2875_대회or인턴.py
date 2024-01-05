'''
여자:남자 = 2:1
N명 여자 M명 남자
K명은 반드시 인턴쉽 프로그램에 참여해야함 따라서 대회 출전 불가
만들수 있는 최대 팀 수
'''
import sys
input = sys.stdin.readline

N, M, K = map(int,input().split())

cnt = 0

# 성별 별로 최대 100명씩 있기 때문에 여학생이 2명씩이라 최대 50팀이다.
for i in range(50):
  if N>=2 and M>=1:
    cnt += 1
    N -= 2
    M -= 1
# for 문을 다 돌리고 나서 이제 k명을 교수님이 차출해야함 차출을 했을 때, 팀이 깨져야 하는 상황이라면 cnt -=1
while K > 0:
  # 여학생 차출
  if N > 0:
    N -= 1
  # 남학생 차출
  elif M > 0:
    M -= 1
  # 팀 해체
  else:
    cnt -= 1
    N += 1
    M += 1 
  K -= 1

print(cnt)