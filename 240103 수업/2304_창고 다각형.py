'''
x 좌표를 기준으로 정렬 후
최고 높이를 구한다.
최고 높이를 기준으로 왼쪽, 오른쪽의 면적을 더한다.
최고 높이가 2개일 경우?
=> 

'''
import sys
input = sys.stdin.readline

N = int(input())
arr = []
for i in range(N):
  x, y = map(int,input().split())
  arr.append([x,y])

arr.sort()

storage = 0
# 가장 첫번째 기둥 설정.
temp_x, temp_y = arr[0]

for pillar in arr:
  x, y = pillar
  #시작은 0,0 에서 시작
  if y > temp_y:
    storage += (x-temp_x) * temp_y
    temp_y = y
  
print(storage)