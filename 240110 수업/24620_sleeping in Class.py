'''
배열A가 주어졌을 때 인접한 인덱스끼리의 합을 하여 몇번의 합으로 모든 A의 배열을 같게 만들 수 있는지
N은 최대 100만
합이 가능한지 알아보려면 0~최대 합까지 확인
'''
import sys
input = sys.stdin.readline

def check(x):
  sum_ = 0
  # 전체 배열을 순회하면서 x를 만들수 있는지를 계속 판별.
  for i in range(n):
    if sum_ > x:
      return False
    sum_ += arr[i]
    # 한번 x를 만들었다면 그 다음 index부터 다시 x를 만들수 있는지 판별하기 위해 sum초기화
    if sum_ == x:
      sum_ = 0
  # 전부 통과가 됐다면 True반환
  return True


T = int(input())
for _ in range(T):
  n = int(input())
  arr = list(map(int,input().split()))
  # 전체 합
  total = sum(arr)
  # 최소 크기는 배열 안에서 가장 큰 수
  min_sum = max(arr)
  # 만약 배열의 최대값이 0이라면 0으로 나눌수 없기 때문에, 1로 설정.
  if min_sum == 0:
    min_sum = 1
  move = 0
  # 최소 크기와 총 합의 범위 사이에서 가능한지를 판별하고 move를 센다.
  for i in range(min_sum,total+1):
    # 모두 같은 숫자로 만들기 위해서는 total의 약수로밖에 만들 수 없다.
    # 따라서 total의 약수이고 그 숫자로 통일하는 것이 가능하다 라고 하면 정답이 될 수 있다.
    # 이때의 move 갯수를 센다.
    if total%i == 0 and check(i):
      # 배열의 모든 원소를 i로 만들었다면, 전체 합을 i로 나눈 만큼으로 쪼개졌을 것이다.
      # 그래서 전체 배열의 갯수에서 몫만큼을 뺀다면 내가 합친 횟수를 계산할 수 있다.
      move = n- total//i
      break
  print(move)