'''

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


n, k = map(int,input().split())
arr = soinsu(k)
# 최대값 갱신
min_cnt = 0

arr2 = list(set(arr))
dict = {}
for i in arr2:
    dict[i] = arr.count(i)

for i in arr2:
  if min_cnt == 0:
      min_cnt = get_k_cnt(n,i)//dict[i]
  else:
    min_cnt = max(get_k_cnt(n,i)//dict[i], min_cnt)
print(min_cnt)