'''
집의 갯수가 홀수인지 짝수인지 판별
집의 갯수가 홀수라면 가운데가 가장 불만이 적은 곳
집의 갯수가 짝수라면 두개 중 작은 값이 불만이 적은 곳
집의 숫자와 상관없이 가운데 범위 내에서는 항상 최소가 됨
'''
import sys
input = sys.stdin.readline

N = int(input())
# 가운데 값을 봐야하니 정렬로 보는것이 좋다
house = sorted(list(map(int,input().split())))

if len(house)%2 == 0:
  # 짝수일때 INDEX는 -1 해주어야함
  index = len(house)//2- 1
else:
  # 홀수일때 index
  index = len(house)//2

answer = house[index]
print(answer)
