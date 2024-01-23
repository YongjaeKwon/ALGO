'''
산성 = 1~10**9
알칼리 -1~-10**9

혼합하여 0에 가장 가까운 용액
산성 + 산성도 가능할 수도있다.
답이 두개 이상일 경우 아무거나 출력.
N = 10만
10만 * 10만
=> 10,000,000,000 백억
=> 줄이자~

'''
import sys
input = sys.stdin.readline

N = int(input())
# 오름차순으로 들어온다.
arr = list(map(int,input().split()))
min_liquid = 10**18
s = 0
e = N-1
liquid_s = arr[s]
liquid_e = arr[e]
while s < e:
  liquid = arr[s] + arr[e]
  if abs(liquid) < min_liquid:
    min_liquid = abs(arr[s] + arr[e])
    liquid_s = arr[s]
    liquid_e = arr[e]
  if liquid == 0:
    break
  if liquid > 0:
    e -= 1
  elif liquid <0:
    s += 1

print(liquid_s, liquid_e)