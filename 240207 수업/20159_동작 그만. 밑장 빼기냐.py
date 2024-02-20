'''

'''
import sys
input = sys.stdin.readline

n = int(input())
arr = [0] + list(map(int,input().split()))
junghoon = [0]
enemy = [0] 
# 홀,짝을 나누어 저장
for i in range(1,n+1):
  if i % 2 == 1:
    junghoon.append(arr[i])
    enemy.append(0)
  else:
    junghoon.append(0)
    enemy.append(arr[i])
# 각각의 누적합 배열 구하기.
prefix_j = [0] * len(junghoon)
for i in range(1,len(junghoon)):
  prefix_j[i] = prefix_j[i-1] + junghoon[i] 

prefix_e = [0] * len(enemy)
for i in range(1,len(enemy)):
  prefix_e[i] = prefix_e[i-1] + enemy[i]

# 아무런 밑장 빼기를 하지 않았을 때의 값을 최대값으로 저장
answer = prefix_j[-1]

# 모든 경우에서 밑장 빼기를 했을 경우를 계산하여 max를 구해서 본다.
for i in range(1,n+1):
  # 원래 받던거에서 밑장을 상대방에게 주면, 정훈이는 짝수번 째의 카드를 가지게 된다.
  if i%2 ==1 :
    temp = prefix_j[i-1] + (prefix_e[-1] - prefix_e[i])
  # 밑장을 정훈이가 가지게 되는 경우
  else:
    temp = prefix_j[i] + (prefix_e[-2] - prefix_e[i-1])
  answer = max(temp,answer)
print(answer)