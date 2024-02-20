'''
길이가 같은 수열 A,B
Ai~Aj의 합 == Bi ~ Bj의 쌍의 개수 (i,j)
구간의 합을 반복
=> 누적합 배열을 통해 get 연산으로 줄이기
N = 2*(10**5)
단순 누적합 배열을 만들어서 2중 for문을 돌게 되면 O(N**2) 시간 초과
어짜피 i,j가 같기때문에 누적합 배열을 2개가 아닌 1개를 만들어 계산 (A에서 B를 뺸 값 저장)
=> 순서쌍을 구하기 위해서 prefix를 순회하면서 차이 값을 dict에 저장. 만약 prefix[i]값이 이미 dict에 존재한다면 == 순서쌍
=> 기존에 존재하던 dict[prefix[i]]값을 cnt에 더해준다.
'''
import sys
from collections import defaultdict
input = sys.stdin.readline
n = int(input())
arr_A = [0] + list(map(int,input().split()))
arr_B = [0] + list(map(int,input().split()))
prefix = [0] * (n+1)
dict = defaultdict(int)
for i in range(1,n+1):
  prefix[i] = prefix[i-1] + arr_A[i] - arr_B[i]

print(prefix)
cnt = 0
for i in range(1,n+1):
  if prefix[i] == 0:
    cnt += 1
  # dict에 차이값을 넣으면서 만약에 존재 한다면, cnt에 차이가 같은 개수만큼 더해주고 dict +=1
  if prefix[i] in dict:
    cnt += dict[prefix[i]]
    dict[prefix[i]] += 1
  else:
    dict[prefix[i]] = 1
print(cnt)