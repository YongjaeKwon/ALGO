'''
n!에서 만들 수 있는 k**i에서 i의 최대값을 구한다!
n!에서 k의 갯수를 구하는 식으로 하면 안되기 때문에 k를 소인수 분해 해서 각 소인수의 갯수 중 가장 적은 갯수를 찾는다. (지수의 최소값 찾기)
=> k가 12, 6일때를 비교해보면 소인수 분해 했을 때, [2,2,3] / [2,3]이 나오는걸 알 수 있다.
따라서 소인수 분해 후 같은 수의 소인수가 여러개 나온다면 이를 고려하여 cnt/2 를 해줬어야한다.
dict로 소인수의 갯수를 체크한 후, 각 get_k_cnt에서 나오는 갯수를 // dict[i]를 통해 해결하였다.
'''
import sys
input = sys.stdin.readline

def get_k_cnt(N,K):
  cnt = 0
  init_K = K
  while K <= N:
    cnt += N//K
    K *= init_K
  return cnt

def soinsu(n):
  arr = []
  x = n
  for i in range(2,n+1):
    if i * i > n:
      break
    if x == 1:
      break
    while x%i == 0:
      arr.append(i)
      x//=i
  # 루트 n보다 큰 소인수가 있다면 n에 아직 남아있기 때문에
  if x != 1:
    arr.append(x)
  return arr

T = int(input())
for _ in range(T):
  n, k = map(int,input().split())
  arr = soinsu(k)
  # k를 소인수 분해 하여 각 소인수를 get_k_cnt 함수를 통해 최소 값을 갱신한다.
  min_cnt = 0

  arr2 = list(set(arr))
  dict = {}
  for i in arr2:
     dict[i] = arr.count(i)
  
  for i in arr2:
    if min_cnt == 0:
        min_cnt = get_k_cnt(n,i)//dict[i]
    else:
      min_cnt = min(get_k_cnt(n,i)//dict[i], min_cnt)
  print(min_cnt)