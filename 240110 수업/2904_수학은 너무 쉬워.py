'''
두 수 A,B를 고르고
A를 나눌수 있는 소수 X를 고른다
A = A/x
B = B*x

=> 무한히 반복했을 때, 점수는 종이에 적혀있는 모든 수의 최대 공약수
=> 가장 큰 최대 공약수를 가지려면 모든 수를 소인수 분해 후, 지수들을 N으로 나눈 몫에서 각 숫자에 부족한 만큼 나누어준다.
'''
import sys
input = sys.stdin.readline
N = int(input())
arr = list(map(int,input().split()))

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
  if x != 1:
    arr.append(x)
  return arr

# dictionary에 전체 소인수들의 갯수를 정리
dict ={}
new_arr = []
for i in range(N):
  temp_arr = soinsu(arr[i])
  new_arr.append(temp_arr)
  for j in range(len(temp_arr)):
    if temp_arr[j] in dict:
      dict[temp_arr[j]] += 1
    else:
      dict[temp_arr[j]] = 1

# 각각 가져가야할 소수의 갯수 구하기
new_dict = {}
for i in dict:
  new_dict[i] = dict[i]//N

# 가져가야할 움직임 기록
move_cnt = 0
for i in range(N):
  for j in new_dict:
    # 모자랄 경우에 가져오는걸로 기록.
    if new_arr[i].count(j) < new_dict[j]:
      move_cnt += new_dict[j] - new_arr[i].count(j)

# 최대 공약수 구하기
answer = 1
for i in new_dict:
  if new_dict[i] != 0:
    answer *= (i ** new_dict[i])

print(answer, move_cnt)