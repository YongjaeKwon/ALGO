import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
# 고장난 버튼이 존재할 때만 입력받기
if m:
  lst = set(input().split())
# 고장난 버튼이 없으면 길이만큼 출력
else:
  lst = set()

# 이미 100번 채널이라면 끝
if n == 100:
  print(0)
  exit()

min_ = abs(100-n) # + - 로만 채널로 이동하는 경우
for target in range(1000001): #큰 번호에서 작은 번호로 이동하는 경우도 고려해야하기 때문에 2배
  for i in str(target):
    # 고장난키가 있다? stop
    if i in lst:
      break
    # 고장난 키가 없으면, 그 번호에서 + - 를 해주면 된다.
  else:
    min_ = min(min_, len(str(target)) + abs(target - n))

print(min_)