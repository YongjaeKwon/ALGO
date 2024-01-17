'''
a,b의 범위 내에서 소수인것 중에 팰린드롬인 것을 찾는다
=> 에라토스테네스의 체로 1억까지의 소수들을 구한다.
True인 것들에 대해서 뒤집어도 똑같다면 출력
=> 범위가 1억이라 메모리 초과가 난다
=> 근데 막상 1억을 넣고 돌려보니 9989899가 가장 마지막 펠린드롬이다.
=> 범위를 줄여서 해보자

'''
import sys
input = sys.stdin.readline

# 에라토스테네스의 체
max_num = 9989899
is_Prime = [True for _ in range(max_num + 1)]
is_Prime[1] = False
for i in range(2,max_num+1):
  if not is_Prime:
    continue
  for j in range(i*i,max_num+1,i):
    is_Prime[j] = False

a,b = map(int,input().split())
if b > max_num:
  b = max_num
for i in range(a,b+1):
  if is_Prime[i]:
    if i == int(str(i)[::-1]):
      print(i)
print(-1)