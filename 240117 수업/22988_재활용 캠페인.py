'''
총 용량 X
A,B를 까져가면 min(A+B+x/2, X) 로 바꿔준다.
모은게 N
i번째 용기에 Ci 만큼 담겨있다.
=> 꽉찬 용기를 몇개 만들 수 있는가?
=> 이미 꽉찬 용기는 교체할 필요 x (cnt에 추가하고 배열에서 제거한다)
=> 병이 한개만 남았을 경우를 고려하지 못했다. (s=e 가 되면 남는병 1개이기 때문에, 추가해줘야한다.) while문의 조건도 s <=e로 변경
=> 위의 조건을  while문 맨 위에서 확인 후 탈출해야함.
'''
import sys
input = sys.stdin.readline

N,X = map(int,input().split())
arr = list(map(int,input().split()))

# 이미 X만큼 가지고 있으면 굳이 바꿀 필요가 없기 때문에 cnt에 추가
cnt = arr.count(X)
# 여기서 최대 10만번 연산 소모
arr = [i for i in arr if i != X]
# 투포인터 사용을 위해 정렬
arr.sort()
# s,e 초기값 설정
s, e = 0, N-1-cnt
# 문제를 보면 조건을 만족하지 못하는 경우 2개를 합치면 1/2*X를 채워준 상태로 주기 때문에 3개를 합치게 될 경우 무조건 온전한 병을 만들 수 있다.
leftover = 0
while s <= e:
  # 병이 1개만 남을 경우를 고려해야함.
  if s == e:
    leftover += 1
    break
  # 1/2 가 넘으면 새로 한병을 만들 수 있기 때문에 cnt += 1
  if arr[s]+ arr[e] >= 0.5 * X:
    cnt += 1
    s += 1
    e -= 1
  # 
  else:
    # 후보군 중 제일 큰것과 결합했을 때, 1/2를 못채우기 때문에 후보군에서 제외
    s += 1
    # 남는 병 한개 누적
    leftover += 1

print(cnt + leftover//3)