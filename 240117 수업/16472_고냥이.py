'''
고냥이 말 번역기
문자열을 N개의 종류의 알파벳을 가진 문자열 밖에 인식하지 못한다.
'''
import sys
input = sys.stdin.readline

N = int(input())
cat = input().rstrip()
# 인덱스
s = 0
e = 0
dict = {}
answer = 0
while e < len(cat):
  # 초기 디폴트 값을 0으로 설정
  dict.setdefault(cat[e], 0)
  dict[cat[e]] += 1
  # dict에 들어있는 알파벳의 갯수가 N보다 커지면 s를 한칸씩 이동하면서 N을 충족할때까지 이동하며 제거
  while len(dict) > N:
    dict[cat[s]] -= 1
    if dict[cat[s]] == 0:
      del dict[cat[s]]
    s += 1
  e += 1
  # 길이 갱신
  answer = max(answer, sum(dict.values()))
print(answer)