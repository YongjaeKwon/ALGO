'''
각 테스트 케이스에서 부분 수열의 합이 d로 나누어 떨어지는 것의 개수
구간 합을 계속해서 반복한다. (구간 get 반복)
=> 미리 누적합 배열을 만들어둔다.
누적합 배열에서 x,y로 이중 for문을 순회하면서 나누어 떨어지는 것들을 cnt +=1 
=> 시간초과
=> prefix의 모듈러 연산을 미리 해둔다
=> 구간 까지의 합을 했을 때 0이다 => 나누어 떨어진다.
=> 구간까지의 합을 두개 뺏을 때 0이다 => 나누어 떨어진다.

'''
import sys
from collections import defaultdict
input = sys.stdin.readline
# testcase
c = int(input())
for _ in range(c):
  d, n = map(int,input().split())
  arr = list(map(int,input().split()))
  # 누적합 배열 만들기
  prefix = [0] * (n+1)
  for i in range(1,n+1):
    # 더해서 나눠도 어짜피 나머지는 유지되니까 %d 하면서 넣어줌
    prefix[i] = (prefix[i-1] + arr[i-1]) % d
  #prefix 배열에서 두 수의 차이가 0인 것을 두개 뽑으면 되는 것. nC2를 해준다.
  # 각 prefix의 숫자를 dict에 저장
  dict = defaultdict(int)
  for i in range(1,n+1):
    dict[prefix[i]] += 1
  # 기존 prefix에 0을 한개 붙여놨으므로 0 한개를 뺴준 상태로 count에 추가
  cnt = dict[0]

  for i in dict.values():
    # value의 갯수를 불러와서 nC2를 한다. == n*(n-1) / 2
    cnt += i * (i-1) // 2
  print(cnt)