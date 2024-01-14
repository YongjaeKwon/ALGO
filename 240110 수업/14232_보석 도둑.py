'''
보석끼리의 무게 == 곱
훔쳐올수 있는 최대 보석의 개수
최대한 많은 수를 가져가야 하므로 소인수 분해를 하여 개수를 카운트 한다.
'''
import sys
input = sys.stdin.readline
K = int(input())

# K가 계속해서 변화하기 때문에 n이라는 변수에 저장 후 n을 변화시킨다.
n = K
# K의 소인수 분해를 하면 된다.
arr = []
cnt = 0
for i in range(2,K+1):
  if i * i > K:
    break
  if n == 1:
    break
  while n%i == 0:
    arr.append(i)
    cnt += 1
    n//=i
if n!=1:
  cnt += 1
  arr.append(n)

print(cnt)
for i in range(len(arr)):
  print(arr[i], end =' ')