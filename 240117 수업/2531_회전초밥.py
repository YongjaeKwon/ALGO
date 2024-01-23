'''
N : 접시의 수
d : 초밥의 가짓수
k : 연속해서 먹는 초밥 갯수
c : 쿠폰 번호
같은 종류의 초밥이 존재한다.
N 최대 300만
d 최대 3000종류
k 연속 최대 3000접시
마지막 초밥부터 먹을 경우, 초반으로 다시 돌아가서 먹는 순환형 구조이기 때문에, 같은 배열을 두개 합쳐준다. (N 최대 600만)
=> 어짜피 K개가 최대이기 때문에 두배만 해주어도 내가 처음 먹은 접시 직전까지가 최대 연속으로 먹은 갯수가 된다.
'''
import sys
input = sys.stdin.readline

N,d,k,c = map(int,input().split())

sushi = []
for _ in range(N):
  sushi.append(int(input()))

# 마지막 초밥부터 먹을 경우, 초반으로 다시 돌아가서 먹는 순환형 구조이기 때문에, 같은 배열을 두개 합쳐준다. (N 최대 600만)
sushi += sushi
# 처음부터 k개 만큼 순회
s = 0
e = k - 1
# 먹은 초밥의 종류 갯수
cnt = 0
# 먹기 시작하는 초밥이 마지막 순서에 있는 초밥이 될때까지 반복
while s <= N-1:
  # 연속으로 k개 만큼 떼와서, 중복을 제거
  eat = list(set(sushi[s:e+1]))
  # 쿠폰에 적힌 번호가 내가 먹은 스시에 없을 경우 1개를 추가로 받게 된다.
  if c in eat:
    cnt = max(cnt, len(eat))
  else:
    cnt = max(cnt,len(eat) + 1)
  # s와 e를 한칸씩 옮겨서 다음 회전초밥 먹어보기
  s += 1
  e += 1

print(cnt)