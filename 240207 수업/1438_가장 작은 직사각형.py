'''
체커와 유사한 문제..!
내부에 점이 몇개 존재하는지를 판단해야하기 때문에 좌표의 범위를 -1부터 10001까지
=> 하지만 모든 범위를 탐색할 필요는 없다.
X의 좌표를 x-1, x+1로 고정시켜두고 y의 범위를 옮겨가며 탐색한다.
'''
import sys
input = sys.stdin.readline

n = int(input())
arr = []
X = []
Y = []
for _ in range(n):
  x, y = map(int,input().split())
  # 모든 x를 볼 필요가 없기 때문에 x-1과 x+1의 범위 내에서만 보면 된다.
  X.append(x-1)
  X.append(x+1)
  Y.append(y-1)
  Y.append(y+1)
  arr.append((x,y))

min_y = min(point[1] for point in arr)
max_y = max(point[1] for point in arr)
Y = list(set(Y))
Y.sort()
length_Y = len(Y)
answer = sys.maxsize
for x1 in X:
  for x2 in X:
    i = 0
    j = 1
    while j < length_Y and i <= j:
      y1 = Y[i]
      y2 = Y[j]
      cnt = 0
      for k in range(n):
        a,b = arr[k]
        # print('a,b',a,b)
        if x1 < a < x2 and y1 < b < y2:
          cnt += 1
      # 점이 충분하면
      if 2*cnt >= n:
        answer = min(answer, (x2-x1) * (y2-y1))
        i += 1
      # 점이 부족하면
      else:
        j += 1

print(answer)

