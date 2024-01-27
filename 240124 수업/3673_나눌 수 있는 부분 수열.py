'''
각 테스트 케이스에서 부분 수열의 합이 d로 나누어 떨어지는 것의 개수
구간 합을 계속해서 반복한다. (구간 get 반복)
=> 미리 누적합 배열을 만들어둔다.
누적합 배열에서 x,y로 이중 for문을 순회하면서 나누어 떨어지는 것들을 cnt +=1 
'''
import sys
input = sys.stdin.readline
# testcase
c = int(input())
for _ in range(c):
  d, n = map(int,input().split())
  arr = list(map(int,input().split()))
  # 누적합 배열 만들기
  prefix = [0] * (n+1)
  for i in range(1,n+1):
    prefix[i] = prefix[i-1] + arr[i-1]
  
  print(prefix)
  cnt = 0
  for i in range(1,n+1):
    for j in range(i+1,n+1):
      if (prefix[i] - prefix[j-1]) % d == 0 and i != j-1:
        print('prefix',prefix[i],prefix[j-1])
        cnt += 1
  print(cnt)