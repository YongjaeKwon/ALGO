'''
T: -10억~10억
배열 A와 B에서 합이 T가 되는 부배열쌍의 개수
n,m: 1~1000
구간의 합과 구간의 합을 더해서 T가 되는 것을 구하는 문제.
구간의 합을 반복하기 때문에 suffix를 두개 이용하여 문제를 풀어본다.
=> 이때 연산 횟수를 가늠해보면 suffix_A와 B를 만드는데 각각 최대 1000번의 연산
=> get 연산은 O(1)이기 때문에 각각에서 부분수열의 합을 구해와서 더해준다면 1000*1000 => 1,000,000 
=> 그럼 각 부분 수열의 합을 완전탐색을 한다면, 1,000,000 * 1,000,000 => 1억번
2초내에 연산 가능
'''
import sys
from collections import defaultdict
input = sys.stdin.readline
T = int(input())
n = int(input())
arr_A = [0] + list(map(int,input().split()))
m = int(input())
arr_B = [0] + list(map(int,input().split()))

answer = 0

prefix_A = [0]*(n+1)
prefix_B = [0]*(m+1)

for i in range(1,n+1):
  prefix_A[i] = prefix_A[i-1] + arr_A[i]

for j in range(1,m+1):
  prefix_B[j] = prefix_B[j-1] + arr_B[j]

# 인덱스의 범위는 1~n까지
# A가 가질 수 있는 부분 수열을 dict에 저장
dict_A = defaultdict(int)
ans_dict = defaultdict(int)

#
for x in range(1,len(prefix_A)):
  for y in range(0,x):
    dict_A[prefix_A[x] - prefix_A[y]] += 1

for x in range(1,len(prefix_B)):
  for y in range(0,x):
    # T에서 prefix_B의 값을 뺸 값이 dict_A에 있다면 그만큼 추가
    temp = T - (prefix_B[x] - prefix_B[y])
    if temp in dict_A:
      answer += dict_A[temp]

print(answer)