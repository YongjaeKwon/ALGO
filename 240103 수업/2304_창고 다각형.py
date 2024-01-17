'''
x 좌표를 기준으로 정렬 후
최고 높이를 구한다.
최고 높이를 기준으로 왼쪽, 오른쪽의 면적을 더한다.
최고 높이가 2개일 경우
중간 구간이 생긴다.
=> 최고 높이 만큼의 면적을 더해주면 된다.

Index Error을 보아하니 기둥이 한개일 때만 존재하는 경우가 있음.
예외처리를 해준다.

'''
import sys
input = sys.stdin.readline

N = int(input())
arr = []
for i in range(N):
  x, y = map(int,input().split())
  arr.append([x,y])

arr.sort()

# 가장 높은 기둥의 높이를 구한다.
highest = 0
for i in arr:
  if highest < i[1]:
    highest = i[1]

# 기둥이 한개일 때 예외처리
  if len(arr) == 1:
    print(highest)
    exit()


# 가장 높은 기둥의 갯수
# 가장 높은 기둥의 x좌표를 담을 arr
highest_x = []
highest_cnt = 0
for i in arr:
  if i[1] == highest:
    highest_cnt +=1
    # arr이 x좌표를 기준으로 정렬되어 있기 때문에 가장 처음 x좌표와 마지막 x좌표를 쉽게 구할 수 있다.
    highest_x.append(i[0])

# 창고 지붕 크기
roof = 0
# 가장 높은 위치의 높이 면적만큼 먼저 구한다.
if highest_cnt > 1:
  roof += highest * (highest_x[-1] - highest_x[0] + 1)

if highest_cnt == 1:
  roof += highest

# 기둥이 오로지 1개일때를 구해야함. (예외처리)


# 가장 첫번째 기둥 설정.
temp_x, temp_y = arr[0]

# 왼쪽
for i in range(1,len(arr)+1):
  x, y = arr[i][0], arr[i][1]
  #시작은 0,0 에서 시작
  if y > temp_y:
    roof += (x-temp_x) * temp_y
    temp_x = x
    temp_y = y
  if temp_y == highest:
    break

temp_x, temp_y = arr[-1]
# 오른쪽
for i in range(len(arr)-2, -1, -1):
  x, y = arr[i][0], arr[i][1]
  if y > temp_y:
    roof += (temp_x - x) * temp_y
    temp_x = x
    temp_y = y
  if temp_y == highest:
    break

print(roof)