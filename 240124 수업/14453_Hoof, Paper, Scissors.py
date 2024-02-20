'''
5
P
P
H
P
S
동작을 한번만 바꿀 떄, 가장 많이 이길 수 있는 횟수.
'''
import sys
input = sys.stdin.readline
#각각을 배열로 저장 하면서 누적합 동시에 구하기
n = int(input())
hoof = [0 for _ in range(n+1)]
paper = [0 for _ in range(n+1)]
scissors = [0 for _ in range(n+1)]
for i in range(1,n+1):
  s = input().rstrip()
  if s == "H":
    hoof[i] = hoof[i-1] + 1
    paper[i] = paper[i-1]
    scissors[i] = scissors[i-1]
  elif s == 'P':
    hoof[i] = hoof[i-1]
    paper[i] = paper[i-1] + 1
    scissors[i] = scissors[i-1]
  elif s == 'S':
    hoof[i] = hoof[i-1]
    paper[i] = paper[i-1]
    scissors[i] = scissors[i-1] + 1

answer = 0
# i번째에서 바꿨을 때, 그때의 최대값을 비교해서 answer에 저장
# 6가지의 경우의 수를 모두 구한다 (hp,hs,ph,ps,sp,sh)
for i in range(1,n+1):
  hp = hoof[i-1] + paper[n] - paper[i-1]
  hs = hoof[i-1] + scissors[n] - scissors[i-1]
  ph = paper[i-1] + hoof[n] - hoof[i-1]
  ps = paper[i-1] + scissors[n] - scissors[i-1]
  sp = scissors[i-1] + paper[n] - paper[i-1]
  sh = scissors[i-1] + hoof[n] - hoof[i-1]
  answer = max(hp,hs,ph,ps,sp,sh,answer)
print(answer)