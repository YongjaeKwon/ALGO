'''
소수 판별 함수를 만들어 True, False를 반환
입력된 숫자 자체가 소수가 아니다 => False
소수다 => 뒤집어서 검증
str로 변경 후 뒤집는 과정은 최대 10**16자리까지 이니 -> 16번 순회 (매우 빠름)
뒤집은 수를 다시 소수 판별 후 yes no 반환
'''
import sys
input = sys.stdin.readline

# 소수 판별
def check(n):
  if n == 1:
    return False
  cnt = 0
  for i in range(2,n+1):
    if i * i > n:
      break
    if n % i == 0:
      cnt += 1
  if cnt == 0:
    return True
  else:
    return False

reverse = {'1': '1', '2': '2', '3': 'x', '4': 'x', '5': '5', '6': '9', '7': 'x', '8': '8', '9': '6', '0': '0'}
N = int(input())

if check(N) == False:
  print('no')
  exit()

N = str(N)
new_str = ''
for i in N:
  # 3 4 7은 숫자가 아니니까 no출력
  if reverse[i] == 'x':
    print('no')
    exit()
  else:
    new_str += reverse[i]
    
new_str = new_str[::-1]
if check(int(new_str)) == False:
  print('no')
else:
  print('yes')