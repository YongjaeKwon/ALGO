'''
공식 보트 C1, C2, C4
C = 카누
숫자 = 사람
공식 경기 200, 500, 1000m

C4의 1000m 경기에 참가 예정
같은 수의 학생 4개의 반, 각반 1명 차출
선수들의 몸무게 합이 특정 값에 근접할때 최대의 성과
특정 값이 200일때 198, 202라면 198이 선택을 받게 됨
1
300 4
60 52 80 40
75 68 88 63
48 93 48 54
56 73 49 75

최대 1000**4
투포인터로 3중으로 만들면 1000*3
=> 1,000,000,000
이렇게 해도 초과

1,2반의 합과 3,4반의 합을 투포인터로.
1,2반의 합 구하기 => 1,000,000
3,4반의 합 구하기 => 1,000,000
O(N**2)번으로 줄일 수 있다.
=> 가능

'''
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
  target, n = map(int,input().split())
  arr = []
  for __ in range(4):
    arr.append(list(map(int,input().split())))

  # 1,2번 / 3,4번 합치기
  arr_12 = []
  arr_34 = []
  for i in range(n):
    for j in range(n):
      arr_12.append(arr[0][i] + arr[1][j])
      arr_34.append(arr[2][i] + arr[3][j])

  # 중복값이 존재할 수 있기 떄문에 set을 사용하여 중복 제거
  # 투포인터 사용을 위해 정렬
  arr_12 = sorted(list(set(arr_12)))
  arr_34 = sorted(list(set(arr_34)))
  
  # 최소 차이 기록할 변수
  min_diff = sys.maxsize
  # 정답 담을 변수
  answer = 0
  # 포인터를 12를 합친 배열의 시작하고 34의 끝에서 시작하여 찾는다. (각각 다른 배열에서의 index를 순회한다.)
  s = 0
  e = len(arr_34)-1
  while s < len(arr_12) and e >= 0:
    diff = arr_12[s] + arr_34[e] - target
    # 차이값의 최소를 갱신하고 정답의 후보를 갱신
    if abs(diff) < min_diff:
      min_diff = abs(diff)
      answer = arr_12[s]+arr_34[e]
    # 차이가 같을 때, 더 작은 숫자를 정답으로 인정해야한다.
    elif abs(diff) == min_diff:
      answer = min(answer, arr_12[s]+arr_34[e])
    # 차이가 0보다 작다면 target에 근접하게 하기위해 s를 한칸 이동시켜서 후보군 좁히기.
    if diff < 0:
      s += 1
    # 차이가 0이라면 그게 정답이니 while문 탈출
    elif diff == 0:
      answer = target
      break
    # 크다면 e를 이동시켜서 후보군 좁히기
    else:
      e -= 1
  print(answer)